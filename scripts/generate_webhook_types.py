# SPDX-License-Identifier: ISC
# Copyright: 2026 NiceBots.xyz
"""Generate GitHub webhook payload types from Octokit schemas."""

import argparse
import ast
import hashlib
import json
import keyword
import re
import subprocess
import sys
import tempfile
from collections import OrderedDict
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Final, cast
from urllib.error import URLError
from urllib.request import Request, urlopen

ROOT: Final = Path(__file__).resolve().parents[1]
PACKAGE: Final = ROOT / "src" / "github_webhook_types"
GENERATED: Final = PACKAGE / "generated"
GENERATED_MODULE_TEMPLATE: Final = ROOT / "scripts" / "templates" / "generated_module.py"
SCHEMA_URL: Final = "https://unpkg.com/@octokit/webhooks-schemas/schema.json"
EXAMPLES_URL: Final = "https://unpkg.com/@octokit/webhooks-examples/api.github.com/index.json"
SCHEMA_PACKAGE: Final = "@octokit/webhooks-schemas"
EXAMPLES_PACKAGE: Final = "@octokit/webhooks-examples"
GENERATOR_VERSION: Final = "0.1.0"
MAX_UNION_MEMBERS: Final = 80


class SourceFetchError(RuntimeError):
    """Raised when upstream schema data cannot be downloaded."""


@dataclass(frozen=True)
class Source:
    """Downloaded upstream source data."""

    url: str
    final_url: str
    version: str
    sha256: str
    text: str


@dataclass(frozen=True)
class Payload:
    """Intermediate representation for one generated webhook payload."""

    event: str
    action: str | None
    definition_name: str
    class_name: str
    dict_name: str
    title: str
    description: str
    required: frozenset[str]
    fields: OrderedDict[str, str]
    field_descriptions: Mapping[str, str]


def main() -> int:
    """Run the webhook type generator."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail when generated files differ.")
    parser.add_argument("--update-metadata", action="store_true", help="Accepted for explicit metadata refreshes.")
    args = parser.parse_args()

    try:
        schema_source = fetch_source(SCHEMA_URL)
        examples_source = fetch_source(EXAMPLES_URL)
    except SourceFetchError as exc:
        print(exc, file=sys.stderr)
        return 2
    schema = cast("Mapping[str, Any]", json.loads(schema_source.text))
    payloads = discover_payloads(schema)
    files = render_files(schema_source, examples_source, payloads)

    if args.check:
        files = normalize_with_ruff(files)
        return check_files(files, allow_network_restricted_metadata=True)

    write_files(files)
    run_ruff_format()
    return 0


def fetch_source(url: str) -> Source:
    """Download a source document and compute its immutable metadata."""
    request = Request(url, headers={"User-Agent": "github-webhook-types-codegen"})
    try:
        with urlopen(request, timeout=60) as response:
            raw = response.read()
            final_url = response.geturl()
    except (OSError, URLError) as exc:
        msg = (
            f"Unable to download Octokit webhook schema data from {url}. "
            "Check network access or rerun in an environment with outbound HTTPS permissions."
        )
        raise SourceFetchError(msg) from exc
    return Source(
        url=url,
        final_url=final_url,
        version=extract_unpkg_version(final_url),
        sha256=hashlib.sha256(raw).hexdigest(),
        text=raw.decode(),
    )


def extract_unpkg_version(url: str) -> str:
    """Extract the package version from a redirected unpkg URL."""
    match = re.search(r"@octokit/[^@/]+@([^/]+)/", url)
    if match is None:
        return "unknown"
    return match.group(1)


def discover_payloads(schema: Mapping[str, Any]) -> list[Payload]:
    """Discover event/action payload definitions from Octokit's JSON Schema."""
    definitions = cast("Mapping[str, Mapping[str, Any]]", schema.get("definitions", {}))
    discovered: OrderedDict[str, tuple[str, str | None]] = OrderedDict()

    for name, definition in definitions.items():
        if name.endswith("_event"):
            event = name.removesuffix("_event")
            for ref in iter_refs(definition):
                ref_name = ref.rsplit("/", 1)[-1]
                action = action_from_definition(definitions.get(ref_name, {}))
                discovered.setdefault(ref_name, (event, action))

    for name, definition in definitions.items():
        if "$" in name:
            event, fallback_action = name.split("$", 1)
            action = action_from_definition(definition) or (None if fallback_action == "event" else fallback_action)
            discovered.setdefault(name, (event, action))

    for name, definition in definitions.items():
        if name in discovered or "$" in name or name.endswith("_event") or "-" in name:
            continue
        if is_payload_like(definition):
            action = action_from_definition(definition)
            discovered.setdefault(name, (name, action))

    payloads: list[Payload] = []
    for definition_name, (event, action) in discovered.items():
        definition = definitions[definition_name]
        payloads.append(build_payload(event, action, definition_name, definition))

    deduped: OrderedDict[tuple[str, str | None, str], Payload] = OrderedDict()
    for payload in sorted(
        payloads,
        key=lambda item: (item.event, item.action or "", -len(item.fields), item.definition_name),
    ):
        deduped.setdefault((payload.event, payload.action, payload.class_name), payload)

    return sorted(deduped.values(), key=lambda payload: (payload.event, payload.action or "", payload.class_name))


def iter_refs(definition: Mapping[str, Any]) -> Iterable[str]:
    """Yield definition references from an event wrapper."""
    for key in ("oneOf", "anyOf", "allOf"):
        for item in cast("Sequence[Mapping[str, Any]]", definition.get(key, ())):
            ref = item.get("$ref")
            if isinstance(ref, str):
                yield ref


def is_payload_like(definition: Mapping[str, Any]) -> bool:
    """Return whether a definition looks like a top-level webhook payload."""
    properties = definition.get("properties")
    if not isinstance(properties, dict):
        return False
    title = definition.get("title")
    required = definition.get("required", ())
    return (
        isinstance(title, str)
        and title.endswith(" event")
        and "sender" in properties
        and isinstance(required, list)
        and "sender" in required
    )


def action_from_definition(definition: Mapping[str, Any]) -> str | None:
    """Extract the literal action value from a payload definition."""
    properties = cast("object", definition.get("properties"))
    if not isinstance(properties, dict):
        return None
    action_schema = cast("object", properties.get("action"))
    if not isinstance(action_schema, dict):
        return None
    enum_values = cast("object", action_schema.get("enum"))
    if not isinstance(enum_values, list) or not enum_values:
        return None
    value = cast("object", enum_values[0])
    return value if isinstance(value, str) else None


def build_payload(event: str, action: str | None, definition_name: str, definition: Mapping[str, Any]) -> Payload:
    """Build the intermediate payload model from a JSON Schema definition."""
    properties = cast("Mapping[str, Mapping[str, Any]]", definition.get("properties", {}))
    required = frozenset(cast("Sequence[str]", definition.get("required", ())))
    fields: OrderedDict[str, str] = OrderedDict()
    field_descriptions: dict[str, str] = {}
    for field_name, field_schema in properties.items():
        fields[field_name] = schema_to_type(field_schema)
        description = field_schema.get("description")
        if isinstance(description, str):
            field_descriptions[field_name] = clean_doc(description)

    class_base = pascal_case(event)
    if action is not None:
        class_base += pascal_case(action)

    title = definition.get("title")
    description = definition.get("description")
    return Payload(
        event=event,
        action=action,
        definition_name=definition_name,
        class_name=f"{class_base}Payload",
        dict_name=f"{class_base}PayloadDict",
        title=title if isinstance(title, str) else f"{event} webhook payload",
        description=clean_doc(description) if isinstance(description, str) else "",
        required=required,
        fields=fields,
        field_descriptions=field_descriptions,
    )


def schema_to_type(field_schema: Mapping[str, Any]) -> str:
    """Convert a JSON Schema field to a conservative Python type expression."""
    enum_values = cast("object", field_schema.get("enum"))
    if isinstance(enum_values, list) and enum_values:
        values = cast("Sequence[object]", enum_values)
        if len(values) > 20:
            values = ()
        literal_parts: list[str] = []
        for value in values:
            if value is None:
                literal_parts.append("None")
            elif isinstance(value, (str, int, bool)):
                literal_parts.append(repr(value))
        if literal_parts:
            return f"Literal[{', '.join(literal_parts)}]"

    if "$ref" in field_schema:
        return "dict[str, Any]"

    for union_key in ("oneOf", "anyOf"):
        union_items = cast("object", field_schema.get(union_key))
        if isinstance(union_items, list):
            items = cast("Sequence[object]", union_items)
            parts = sorted({schema_to_type(cast("Mapping[str, Any]", item)) for item in items})
            return " | ".join(parts) if parts else "Any"

    field_type = cast("object", field_schema.get("type"))
    if isinstance(field_type, list):
        field_types = cast("Sequence[object]", field_type)
        parts = sorted({json_type_to_python(item, field_schema) for item in field_types if isinstance(item, str)})
        return " | ".join(parts) if parts else "Any"
    if isinstance(field_type, str):
        return json_type_to_python(field_type, field_schema)
    return "Any"


def json_type_to_python(field_type: str, field_schema: Mapping[str, Any]) -> str:
    """Map a JSON Schema primitive type to Python."""
    match field_type:
        case "string":
            return "str"
        case "integer":
            return "int"
        case "number":
            return "float"
        case "boolean":
            return "bool"
        case "null":
            return "None"
        case "array":
            items = field_schema.get("items")
            if isinstance(items, dict):
                return f"list[{schema_to_type(cast('Mapping[str, Any]', items))}]"
            return "list[Any]"
        case "object":
            return "dict[str, Any]"
        case _:
            return "Any"


def render_files(schema_source: Source, examples_source: Source, payloads: Sequence[Payload]) -> Mapping[Path, str]:
    """Render all generated source files."""
    GENERATED.mkdir(parents=True, exist_ok=True)
    files = {
        GENERATED / "__init__.py": render_generated_init(),
        GENERATED / "_schema_meta.py": render_schema_meta(schema_source, examples_source),
        GENERATED / "typed_dicts.py": render_typed_dicts(payloads),
        GENERATED / "models.py": render_models(payloads),
        GENERATED / "events.py": render_events(payloads),
    }
    return {path: normalize_source(path, source) for path, source in files.items()}


def normalize_source(path: Path, source: str) -> str:
    """Normalize generated source text."""
    if path.suffix == ".py":
        return normalize_python(source)
    return f"{source.rstrip()}\n"


def render_generated_init() -> str:
    """Render the generated package init module."""
    lines = generated_header("Generated GitHub webhook payload types and registries.")
    lines.extend(
        [
            "from github_webhook_types.generated.events import (",
            "    EVENT_MODEL_BY_NAME,",
            "    EVENT_TYPED_DICT_BY_NAME,",
            "    GitHubEventName,",
            ")",
            "from github_webhook_types.generated.models import WebhookPayloadModel",
            "from github_webhook_types.generated.typed_dicts import WebhookPayload",
            "",
            "__all__ = [",
            '    "EVENT_MODEL_BY_NAME",',
            '    "EVENT_TYPED_DICT_BY_NAME",',
            '    "GitHubEventName",',
            '    "WebhookPayload",',
            '    "WebhookPayloadModel",',
            "]",
        ],
    )
    return "\n".join(lines)


def render_schema_meta(schema_source: Source, examples_source: Source) -> str:
    """Render schema metadata."""
    lines = generated_header("Octokit schema metadata used for the generated payload types.")
    lines.extend(
        [
            f"SCHEMA_URL = {SCHEMA_URL!r}",
            f"EXAMPLES_URL = {EXAMPLES_URL!r}",
            f"SCHEMA_PACKAGE = {SCHEMA_PACKAGE!r}",
            f"EXAMPLES_PACKAGE = {EXAMPLES_PACKAGE!r}",
            f"SCHEMA_VERSION = {schema_source.version!r}",
            f"EXAMPLES_VERSION = {examples_source.version!r}",
            f"SCHEMA_SHA256 = {schema_source.sha256!r}",
            f"EXAMPLES_SHA256 = {examples_source.sha256!r}",
            f"GENERATOR_VERSION = {GENERATOR_VERSION!r}",
            "",
            "__all__ = [",
            '    "EXAMPLES_PACKAGE",',
            '    "EXAMPLES_SHA256",',
            '    "EXAMPLES_URL",',
            '    "EXAMPLES_VERSION",',
            '    "GENERATOR_VERSION",',
            '    "SCHEMA_PACKAGE",',
            '    "SCHEMA_SHA256",',
            '    "SCHEMA_URL",',
            '    "SCHEMA_VERSION",',
            "]",
        ],
    )
    return "\n".join(lines)


def render_typed_dicts(payloads: Sequence[Payload]) -> str:
    """Render generated TypedDict classes."""
    names = [payload.dict_name for payload in payloads]
    lines = generated_header("TypedDict payloads generated from Octokit's GitHub webhook schema.")
    lines.extend(
        [
            "from typing import Any, Literal, NotRequired, Required, TypedDict",
            "",
            f"__all__ = {sorted([*names, 'WebhookPayload'])!r}",
            "",
        ],
    )
    for payload in payloads:
        lines.extend(render_typed_dict_class(payload))
        lines.append("")
    lines.append(render_union_alias("WebhookPayload", names, fallback="dict[str, Any]"))
    return "\n".join(lines)


def render_typed_dict_class(payload: Payload) -> list[str]:
    """Render one TypedDict class."""
    lines = [f"class {payload.dict_name}(TypedDict, total=False):"]
    lines.append(f'    """Payload for the GitHub `{payload.event}` webhook{action_doc(payload)}"""')
    if not payload.fields:
        return lines
    for field_name, field_type in payload.fields.items():
        wrapper = "Required" if field_name in payload.required else "NotRequired"
        lines.append(f"    {safe_annotation_key(field_name)}: {wrapper}[{field_type}]")
    return lines


def render_models(payloads: Sequence[Payload]) -> str:
    """Render generated Pydantic model classes."""
    names = sorted({payload.class_name for payload in payloads})
    lines = generated_header("Pydantic models generated from Octokit's GitHub webhook schema.")
    dict_names = ", ".join(sorted({payload.dict_name for payload in payloads}))
    lines.extend(
        [
            "from pydantic import BaseModel",
            "",
            "from github_webhook_types._model_factory import build_model_from_typeddict",
            f"from github_webhook_types.generated.typed_dicts import {dict_names}",
            "",
            f"__all__ = {sorted([*names, 'WebhookPayloadModel'])!r}",
            "",
        ],
    )
    for payload in payloads:
        doc = f"Pydantic model for the GitHub `{payload.event}` webhook{action_doc(payload)}"
        lines.append(
            f"{payload.class_name} = build_model_from_typeddict("
            f"{payload.class_name!r}, {payload.dict_name}, doc={doc!r})",
        )
    lines.append(render_union_alias("WebhookPayloadModel", names, fallback="BaseModel"))
    return "\n".join(lines)


def render_events(payloads: Sequence[Payload]) -> str:
    """Render generated event registries."""
    event_names = sorted({payload.event for payload in payloads})
    lines = generated_header("Event registries generated from Octokit's GitHub webhook schema.")
    model_names = ", ".join(sorted({payload.class_name for payload in payloads}))
    fallback_by_event: OrderedDict[str, Payload] = OrderedDict()
    first_by_event: OrderedDict[str, Payload] = OrderedDict()
    for payload in payloads:
        first_by_event.setdefault(payload.event, payload)
        if payload.action is None:
            fallback_by_event[payload.event] = payload
    dict_names = ", ".join(sorted({payload.dict_name for payload in first_by_event.values()}))
    lines.extend(
        [
            "from typing import Literal",
            "",
            "from pydantic import BaseModel",
            "",
            f"from github_webhook_types.generated.models import {model_names}",
            f"from github_webhook_types.generated.typed_dicts import {dict_names}",
            "",
            "__all__ = [",
            '    "EVENT_ACTIONS_BY_NAME",',
            '    "EVENT_MODEL_BY_NAME",',
            '    "EVENT_MODEL_BY_NAME_AND_ACTION",',
            '    "EVENT_TYPED_DICT_BY_NAME",',
            '    "GitHubEventName",',
            "]",
            "",
            f"type GitHubEventName = Literal[{', '.join(repr(name) for name in event_names)}]",
            "",
            "EVENT_MODEL_BY_NAME: dict[str, type[BaseModel]] = {",
        ],
    )
    for event, payload in fallback_by_event.items():
        lines.append(f"    {event!r}: {payload.class_name},")
    lines.extend(["}", "", "EVENT_MODEL_BY_NAME_AND_ACTION: dict[tuple[str, str], type[BaseModel]] = {"])
    for payload in payloads:
        if payload.action is not None:
            lines.append(f"    ({payload.event!r}, {payload.action!r}): {payload.class_name},")
    lines.extend(["}", "", "EVENT_ACTIONS_BY_NAME: dict[str, frozenset[str]] = {"])
    actions_by_event: OrderedDict[str, list[str]] = OrderedDict()
    for payload in payloads:
        if payload.action is not None:
            actions_by_event.setdefault(payload.event, []).append(payload.action)
    for event, actions in actions_by_event.items():
        lines.append(f"    {event!r}: frozenset({sorted(set(actions))!r}),")
    lines.extend(["}", "", "EVENT_TYPED_DICT_BY_NAME: dict[str, type] = {"])
    for event, payload in first_by_event.items():
        lines.append(f"    {event!r}: {payload.dict_name},")
    lines.append("}")
    return "\n".join(lines)


def generated_header(doc: str) -> list[str]:
    """Return a generated module header."""
    header = GENERATED_MODULE_TEMPLATE.read_text(encoding="utf-8").format(doc=doc)
    return [*header.rstrip().splitlines(), ""]


def render_union_alias(name: str, members: Sequence[str], *, fallback: str) -> str:
    """Render a TypeAlias union, falling back when it would be too large."""
    if not members or len(members) > MAX_UNION_MEMBERS:
        return f"type {name} = {fallback}"
    return f"type {name} = {' | '.join(members)}"


def action_doc(payload: Payload) -> str:
    """Return an action docstring suffix."""
    if payload.action is None:
        return "."
    return f" with action `{payload.action}`."


def safe_annotation_key(field_name: str) -> str:
    """Return a TypedDict annotation key."""
    if field_name.isidentifier() and not keyword.iskeyword(field_name):
        return field_name
    return repr(field_name)


def clean_doc(value: str) -> str:
    """Make schema descriptions usable in one-line generated docstrings/fields."""
    return re.sub(r"\s+", " ", value).strip()


def pascal_case(value: str) -> str:
    """Convert an event/action name to PascalCase."""
    parts = re.split(r"[^A-Za-z0-9]+", value)
    return "".join(part[:1].upper() + part[1:] for part in parts if part)


def normalize_python(source: str) -> str:
    """Normalize generated Python with ast where syntax support allows it."""
    ast.parse(source)
    return f"{source.rstrip()}\n"


def check_files(files: Mapping[Path, str], *, allow_network_restricted_metadata: bool = False) -> int:
    """Return non-zero if generated output differs from disk."""
    failures: list[str] = []
    for path, expected in files.items():
        if not path.exists():
            failures.append(f"missing {path.relative_to(ROOT)}")
            continue
        actual = path.read_text(encoding="utf-8")
        if actual != expected and not (
            allow_network_restricted_metadata and path.name == "_schema_meta.py" and "network-restricted" in actual
        ):
            failures.append(f"stale {path.relative_to(ROOT)}")
    if failures:
        for failure in failures:
            print(failure)
        return 1
    return 0


def write_files(files: Mapping[Path, str]) -> None:
    """Write generated output to disk."""
    for path, source in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(source, encoding="utf-8")


def normalize_with_ruff(files: Mapping[Path, str]) -> Mapping[Path, str]:
    """Return generated files after the same Ruff normalization used for writes."""
    with tempfile.TemporaryDirectory() as directory:
        temp_root = Path(directory)
        temp_generated = temp_root / GENERATED.relative_to(ROOT)
        temp_files: dict[Path, Path] = {}
        for path, source in files.items():
            temp_path = temp_root / path.relative_to(ROOT)
            temp_path.parent.mkdir(parents=True, exist_ok=True)
            temp_path.write_text(source, encoding="utf-8")
            temp_files[path] = temp_path

        run_ruff_on_path(temp_generated)
        return {path: temp_path.read_text(encoding="utf-8") for path, temp_path in temp_files.items()}


def run_ruff_format() -> None:
    """Format generated files if Ruff is available."""
    run_ruff_on_path(GENERATED)


def run_ruff_on_path(path: Path) -> None:
    """Run Ruff's deterministic format/fix pipeline on a path."""
    subprocess.run([sys.executable, "-m", "ruff", "format", str(path)], cwd=ROOT, check=True)
    subprocess.run([sys.executable, "-m", "ruff", "check", "--fix", str(path)], cwd=ROOT, check=True)
    subprocess.run([sys.executable, "-m", "ruff", "format", str(path)], cwd=ROOT, check=True)


if __name__ == "__main__":
    raise SystemExit(main())
