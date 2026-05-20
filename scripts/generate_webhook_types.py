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
from collections import OrderedDict, deque
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Final, cast
from urllib.error import URLError
from urllib.request import Request, urlopen

ROOT: Final = Path(__file__).resolve().parents[1]
PACKAGE: Final = ROOT / "src" / "github_webhook_types"
GENERATED: Final = PACKAGE / "generated"
GENERATED_MODULE_TEMPLATE: Final = ROOT / "scripts" / "templates" / "generated_module.py"
SCHEMA_URL: Final = "https://unpkg.com/@octokit/openapi-webhooks/generated/api.github.com.json"
SCHEMA_PACKAGE: Final = "@octokit/openapi-webhooks"
GENERATOR_VERSION: Final = "0.3.0"
MAX_UNION_MEMBERS: Final = 80

# Shared-definition rename map. Octokit's OpenAPI uses names like `repository-webhooks` /
# `simple-user` that pascal-case to bulky symbols; this table maps them to the conventional
# short forms our public API exposes. Anything not listed falls back to plain pascal_case.
SHARED_NAME_RENAMES: Final[Mapping[str, str]] = {
    "repository-webhooks": "Repository",
    "simple-user": "User",
    "simple-installation": "Installation",
    "enterprise-webhooks": "Enterprise",
    "organization-simple-webhooks": "Organization",
}

# Hand-maintained overrides for genuine schema gaps. Keyed by `(class_name, field_name)`
# (class names are stable across regenerations; raw schema keys for synthesized inline
# definitions are not). Add entries narrowly only when a real or canonical payload
# demonstrates the upstream `required` claim does not match reality.
#
# Current entries come from `webhook-push` and the three `webhook-workflow-run-*` schemas,
# which inline their `repository` / `workflow_run` shapes and mark fields as required that
# the Octokit canonical example fixtures (committed under tests/fixtures/) do not emit.
FORCED_OPTIONAL: Final[frozenset[tuple[str, str]]] = frozenset(
    {
        ("PushPayloadRepository", "topics"),
        ("PushPayloadRepository", "visibility"),
        ("PushPayloadRepository", "has_discussions"),
        ("WorkflowRunCompletedPayloadWorkflowRun", "triggering_actor"),
        ("WorkflowRunCompletedPayloadWorkflowRun", "actor"),
        ("WorkflowRunCompletedPayloadWorkflowRun", "path"),
        ("WorkflowRunInProgressPayloadWorkflowRun", "triggering_actor"),
        ("WorkflowRunInProgressPayloadWorkflowRun", "actor"),
        ("WorkflowRunInProgressPayloadWorkflowRun", "path"),
        ("WorkflowRunRequestedPayloadWorkflowRun", "triggering_actor"),
        ("WorkflowRunRequestedPayloadWorkflowRun", "actor"),
        ("WorkflowRunRequestedPayloadWorkflowRun", "path"),
    }
)
FORCED_INJECTIONS: Final[Sequence[tuple[str, str, Mapping[str, Any]]]] = cast(
    "Sequence[tuple[str, str, Mapping[str, Any]]]", ()
)


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


@dataclass
class FieldSpec:
    """One property on a generated Definition."""

    type_expr: str  # TypedDict-flavored annotation; references look like `RepositoryDict`
    required: bool
    description: str | None = None


@dataclass
class Definition:
    """Intermediate representation for one generated TypedDict / Pydantic model pair."""

    schema_key: str  # registry key (schema definition name, or synthetic for hoisted inlines)
    class_name: str  # Pydantic class name, e.g. "Repository", "PushPayload"
    dict_name: str  # TypedDict class name, e.g. "RepositoryDict", "PushPayloadDict"
    title: str
    description: str
    is_event_payload: bool
    event: str | None = None
    action: str | None = None
    fields: "OrderedDict[str, FieldSpec]" = field(default_factory=OrderedDict)


def main() -> int:
    """Run the webhook type generator."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail when generated files differ.")
    parser.add_argument("--update-metadata", action="store_true", help="Accepted for explicit metadata refreshes.")
    args = parser.parse_args()

    try:
        schema_source = fetch_source(SCHEMA_URL)
    except SourceFetchError as exc:
        print(exc, file=sys.stderr)
        return 2
    schema = cast("Mapping[str, Any]", json.loads(schema_source.text))
    generator = Generator(schema)
    generator.build()
    files = render_files(schema_source, generator)

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


class Generator:
    """Owns the registry of materialized Definitions and resolves the full reachable type graph.

    Walks every event payload schema, discovers $refs and inline objects transitively, and
    assigns stable class/dict names. Type aliases (non-object schemas referenced by $ref) are
    inlined at the use site rather than materialized as classes.
    """

    def __init__(self, schema: Mapping[str, Any]) -> None:
        self.schema = schema
        components = cast("Mapping[str, Any]", schema.get("components", {}))
        self.raw_definitions: Mapping[str, Mapping[str, Any]] = cast(
            "Mapping[str, Mapping[str, Any]]",
            components.get("schemas", {}),
        )
        self.registry: OrderedDict[str, Definition] = OrderedDict()
        self.inline_definitions: dict[str, Mapping[str, Any]] = {}
        # Pre-claim rename targets so any pascal-collision (e.g. standalone `repository`
        # against renamed `repository-webhooks`) auto-suffixes the *collider*, not the
        # webhook variant we deliberately renamed.
        self.taken_class_names: set[str] = set(SHARED_NAME_RENAMES.values())
        self.taken_dict_names: set[str] = {f"{name}Dict" for name in SHARED_NAME_RENAMES.values()}
        self._pending: deque[str] = deque()
        self._built: set[str] = set()
        self._alias_stack: set[str] = set()  # cycle guard for inlined type aliases

    # ------------------------------------------------------------------ build

    def build(self) -> None:
        """Discover event payloads and transitively materialize the reachable type graph."""
        for definition in discover_event_payloads(self.schema):
            self._register_event_payload(*definition)
        while self._pending:
            key = self._pending.popleft()
            if key in self._built:
                continue
            self._built.add(key)
            self._build_fields(key)
        self._apply_forced_overrides()

    def _apply_forced_overrides(self) -> None:
        """Apply hand-maintained overrides keyed by class_name after the graph is built."""
        by_class_name = {defn.class_name: defn for defn in self.registry.values()}
        for class_name, fname, field_schema in FORCED_INJECTIONS:
            defn = by_class_name.get(class_name)
            if defn is None or fname in defn.fields:
                continue
            type_expr = self._schema_to_type(field_schema, owner=defn, field_name=fname)
            description = field_schema.get("description")
            defn.fields[fname] = FieldSpec(
                type_expr=type_expr,
                required=False,
                description=clean_doc(description) if isinstance(description, str) else None,
            )
        for class_name, fname in FORCED_OPTIONAL:
            defn = by_class_name.get(class_name)
            if defn is None:
                continue
            spec = defn.fields.get(fname)
            if spec is not None:
                spec.required = False

    def _build_fields(self, key: str) -> None:
        defn = self.registry[key]
        schema = self._schema_for(key)
        properties = cast("Mapping[str, Mapping[str, Any]]", schema.get("properties", {}))
        required = frozenset(cast("Sequence[str]", schema.get("required", ())))
        for field_name, field_schema in properties.items():
            type_expr = self._schema_to_type(field_schema, owner=defn, field_name=field_name)
            description = field_schema.get("description")
            defn.fields[field_name] = FieldSpec(
                type_expr=type_expr,
                required=field_name in required,
                description=clean_doc(description) if isinstance(description, str) else None,
            )

    def _schema_for(self, key: str) -> Mapping[str, Any]:
        if key in self.raw_definitions:
            return self.raw_definitions[key]
        return self.inline_definitions[key]

    # ----------------------------------------------------------- registration

    def _register_event_payload(self, event: str, action: str | None, definition_name: str) -> Definition:
        class_base = pascal_case(event)
        if action is not None:
            class_base += pascal_case(action)
        class_name = self._unique_class_name(f"{class_base}Payload")
        dict_name = self._unique_dict_name(f"{class_base}PayloadDict")
        definition_schema = self.raw_definitions[definition_name]
        title = definition_schema.get("title")
        description = definition_schema.get("description")
        defn = Definition(
            schema_key=definition_name,
            class_name=class_name,
            dict_name=dict_name,
            title=title if isinstance(title, str) else f"{event} webhook payload",
            description=clean_doc(description) if isinstance(description, str) else "",
            is_event_payload=True,
            event=event,
            action=action,
        )
        self.registry[definition_name] = defn
        self._pending.append(definition_name)
        return defn

    def _register_shared_definition(self, definition_name: str) -> Definition:
        if definition_name in self.registry:
            return self.registry[definition_name]
        definition_schema = self.raw_definitions[definition_name]
        title = definition_schema.get("title")
        description = definition_schema.get("description")
        rename = SHARED_NAME_RENAMES.get(definition_name)
        if rename is not None:
            # Rename targets are pre-claimed in __init__; bypass the unique check.
            class_base = rename
            class_name = rename
            dict_name = f"{rename}Dict"
        else:
            class_base = pascal_case(definition_name)
            class_name = self._unique_class_name(class_base)
            dict_name = self._unique_dict_name(f"{class_base}Dict")
        defn = Definition(
            schema_key=definition_name,
            class_name=class_name,
            dict_name=dict_name,
            title=title if isinstance(title, str) else class_base,
            description=clean_doc(description) if isinstance(description, str) else "",
            is_event_payload=False,
        )
        self.registry[definition_name] = defn
        self._pending.append(definition_name)
        return defn

    def _register_inline(
        self,
        schema: Mapping[str, Any],
        *,
        owner: Definition,
        suggested_name: str,
    ) -> Definition:
        synthetic_key = f"__inline__::{owner.class_name}::{suggested_name}::{id(schema):x}"
        if synthetic_key in self.registry:
            return self.registry[synthetic_key]
        title = schema.get("title")
        description = schema.get("description")
        class_name = self._unique_class_name(f"{owner.class_name}{suggested_name}")
        dict_name = self._unique_dict_name(f"{class_name}Dict")
        defn = Definition(
            schema_key=synthetic_key,
            class_name=class_name,
            dict_name=dict_name,
            title=title if isinstance(title, str) else class_name,
            description=clean_doc(description) if isinstance(description, str) else "",
            is_event_payload=False,
        )
        self.registry[synthetic_key] = defn
        self.inline_definitions[synthetic_key] = schema
        self._pending.append(synthetic_key)
        return defn

    def _unique_class_name(self, candidate: str) -> str:
        return self._unique(candidate, self.taken_class_names)

    def _unique_dict_name(self, candidate: str) -> str:
        return self._unique(candidate, self.taken_dict_names)

    @staticmethod
    def _unique(candidate: str, taken: set[str]) -> str:
        if candidate not in taken:
            taken.add(candidate)
            return candidate
        suffix = 2
        while f"{candidate}{suffix}" in taken:
            suffix += 1
        chosen = f"{candidate}{suffix}"
        taken.add(chosen)
        return chosen

    # ------------------------------------------------------- type resolution

    def _schema_to_type(  # noqa: PLR0912 -- one fan-out over JSON Schema constructs; splitting would obscure
        self,
        schema: Mapping[str, Any],
        *,
        owner: Definition,
        field_name: str,
    ) -> str:
        """Convert a JSON Schema fragment to a Python type expression in TypedDict flavor."""
        enum_values = cast("object", schema.get("enum"))
        if isinstance(enum_values, list) and enum_values:
            values = cast("Sequence[object]", enum_values)
            if len(values) <= 20:
                literal_parts: list[str] = []
                has_none = False
                for value in values:
                    if value is None:
                        has_none = True
                    elif isinstance(value, (str, int, bool)):
                        literal_parts.append(repr(value))
                if literal_parts:
                    expr = f"Literal[{', '.join(literal_parts)}]"
                    return f"{expr} | None" if has_none else expr
                if has_none:
                    return "None"

        ref = schema.get("$ref")
        if isinstance(ref, str):
            return self._resolve_ref(ref, owner=owner, field_name=field_name)

        for union_key in ("oneOf", "anyOf"):
            union_items = schema.get(union_key)
            if isinstance(union_items, list):
                parts: list[str] = []
                seen: set[str] = set()
                items = cast("Sequence[object]", union_items)
                for index, raw_item in enumerate(items):
                    if not isinstance(raw_item, Mapping):
                        continue
                    item = cast("Mapping[str, Any]", raw_item)
                    branch_name = pascal_case(field_name) + f"Option{index + 1}"
                    part = self._schema_to_type(
                        item,
                        owner=owner,
                        field_name=branch_name if needs_inline_promotion(item) else field_name,
                    )
                    if part not in seen:
                        seen.add(part)
                        parts.append(part)
                parts = simplify_union(parts)
                parts.sort()
                return " | ".join(parts) if parts else "Any"

        field_type = schema.get("type")
        if isinstance(field_type, list):
            field_types = cast("Sequence[object]", field_type)
            scalar_parts = sorted({json_primitive_to_python(item) for item in field_types if isinstance(item, str)})
            return " | ".join(scalar_parts) if scalar_parts else "Any"
        if isinstance(field_type, str):
            return self._json_type_to_python(field_type, schema, owner=owner, field_name=field_name)

        # No `type` / `$ref` / `oneOf` / `anyOf` / `enum`: opaque fallback.
        return "Any"

    def _resolve_ref(self, ref: str, *, owner: Definition, field_name: str) -> str:
        target = ref.rsplit("/", 1)[-1]
        if target not in self.raw_definitions:
            return "Any"

        # Definitions that carry `properties` become their own TypedDict class.
        if has_object_properties(self.raw_definitions[target]):
            if target in self.registry:
                return self.registry[target].dict_name
            return self._register_shared_definition(target).dict_name

        # Type aliases (scalar / array / union schemas without properties): inline.
        if target in self._alias_stack:
            return "Any"
        self._alias_stack.add(target)
        try:
            return self._schema_to_type(self.raw_definitions[target], owner=owner, field_name=field_name)
        finally:
            self._alias_stack.discard(target)

    def _json_type_to_python(
        self,
        field_type: str,
        schema: Mapping[str, Any],
        *,
        owner: Definition,
        field_name: str,
    ) -> str:
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
                items = schema.get("items")
                if isinstance(items, Mapping):
                    inner = self._schema_to_type(
                        cast("Mapping[str, Any]", items),
                        owner=owner,
                        field_name=singularize(field_name),
                    )
                    return f"list[{inner}]"
                return "list[Any]"
            case "object":
                if has_object_properties(schema):
                    suggested = pascal_case(field_name) or "Object"
                    return self._register_inline(schema, owner=owner, suggested_name=suggested).dict_name
                return "dict[str, Any]"
            case _:
                return "Any"


# ---------------------------------------------------------------------- schema helpers


def has_object_properties(definition: Mapping[str, Any]) -> bool:
    """Return whether a definition is an object schema with named properties."""
    if definition.get("type") not in (None, "object"):
        return False
    properties = cast("object", definition.get("properties"))
    if not isinstance(properties, Mapping):
        return False
    return len(cast("Mapping[str, Any]", properties)) > 0


def needs_inline_promotion(schema: Mapping[str, Any]) -> bool:
    """Return whether a union branch should get its own inline-object class name."""
    return schema.get("type") == "object" and isinstance(schema.get("properties"), Mapping)


def discover_event_payloads(schema: Mapping[str, Any]) -> list[tuple[str, str | None, str]]:
    """Discover (event, action, definition_name) triples from an OpenAPI 3.1 spec.

    Iterates `webhooks` entries; each maps to a `webhook-*` schema via
    `post.requestBody.content["application/json"].schema.$ref`. The event name is
    extracted from the operation's `externalDocs.url` fragment (matches GitHub's
    `X-GitHub-Event` header value, e.g. `pull_request_review_comment`). The action
    is the literal value of the payload's `action.enum[0]` when present.
    """
    webhooks = cast("Mapping[str, Mapping[str, Any]]", schema.get("webhooks", {}))
    components = cast("Mapping[str, Any]", schema.get("components", {}))
    definitions = cast("Mapping[str, Mapping[str, Any]]", components.get("schemas", {}))
    discovered: OrderedDict[str, tuple[str, str | None]] = OrderedDict()
    for key, entry in webhooks.items():
        operation = cast("Mapping[str, Any]", entry.get("post", {}))
        ref = (
            cast("Mapping[str, Any]", operation.get("requestBody", {}))
            .get("content", {})
            .get("application/json", {})
            .get("schema", {})
            .get("$ref")
        )
        if not isinstance(ref, str):
            continue
        defn_name = ref.rsplit("/", 1)[-1]
        event = _event_name_from_operation(operation) or key
        action = action_from_definition(definitions.get(defn_name, {}))
        discovered.setdefault(defn_name, (event, action))
    triples = [(event, action, defn_name) for defn_name, (event, action) in discovered.items()]
    triples.sort(key=lambda item: (item[0], item[1] or "", item[2]))
    return triples


def _event_name_from_operation(operation: Mapping[str, Any]) -> str | None:
    external_docs = operation.get("externalDocs")
    if not isinstance(external_docs, Mapping):
        return None
    url = cast("Mapping[str, Any]", external_docs).get("url")
    if not isinstance(url, str):
        return None
    fragment_match = re.search(r"#(.+)$", url)
    return fragment_match.group(1) if fragment_match else None


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


def json_primitive_to_python(field_type: str) -> str:
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
        case _:
            return "Any"


# ---------------------------------------------------------------------- dep graph + topology


def collect_dependencies(defn: Definition, by_dict_name: Mapping[str, str]) -> set[str]:
    """Return the set of schema_keys this Definition's annotations refer to."""
    deps: set[str] = set()
    # Trailing digits in the token cover auto-suffixed renames like `RepositoryDict2`.
    for field_spec in defn.fields.values():
        for token in re.findall(r"\b[A-Z][A-Za-z0-9]*Dict[0-9]*\b", field_spec.type_expr):
            target = by_dict_name.get(token)
            if target is not None and target != defn.schema_key:
                deps.add(target)
    return deps


def topological_sort(registry: Mapping[str, Definition]) -> tuple[list[str], dict[str, set[str]]]:
    """Return (order, forward_refs).

    `order` is a render order minimizing forward references; `forward_refs[key]` is the
    set of dict names that must be quoted from inside the class identified by `key`.
    """
    by_dict_name = {defn.dict_name: defn.schema_key for defn in registry.values()}
    dep_map = {key: collect_dependencies(defn, by_dict_name) for key, defn in registry.items()}

    indegree = dict.fromkeys(registry, 0)
    reverse: dict[str, set[str]] = {key: set() for key in registry}
    for key, deps in dep_map.items():
        for d in deps:
            reverse[d].add(key)
            indegree[key] += 1

    ready: list[str] = sorted(k for k, n in indegree.items() if n == 0)
    order: list[str] = []
    while ready:
        node = ready.pop(0)
        order.append(node)
        for downstream in sorted(reverse[node]):
            indegree[downstream] -= 1
            if indegree[downstream] == 0:
                ready.append(downstream)

    # Anything still unordered participates in a cycle. Append in stable order.
    remaining = sorted(k for k in registry if k not in set(order))
    order.extend(remaining)

    position = {key: index for index, key in enumerate(order)}
    forward_refs: dict[str, set[str]] = {}
    for key, deps in dep_map.items():
        for target in deps:
            if position[target] >= position[key]:
                forward_refs.setdefault(key, set()).add(registry[target].dict_name)
    return order, forward_refs


# ---------------------------------------------------------------------- rendering


def render_files(
    schema_source: Source,
    generator: Generator,
) -> Mapping[Path, str]:
    """Render all generated source files."""
    GENERATED.mkdir(parents=True, exist_ok=True)
    order, forward_refs = topological_sort(generator.registry)
    files = {
        GENERATED / "__init__.py": render_generated_init(),
        GENERATED / "_schema_meta.py": render_schema_meta(schema_source),
        GENERATED / "typed_dicts.py": render_typed_dicts(generator, order, forward_refs),
        GENERATED / "models.py": render_models(generator, order, forward_refs),
        GENERATED / "events.py": render_events(generator),
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


def render_schema_meta(schema_source: Source) -> str:
    """Render schema metadata."""
    lines = generated_header("Octokit schema metadata used for the generated payload types.")
    lines.extend(
        [
            f"SCHEMA_URL = {SCHEMA_URL!r}",
            f"SCHEMA_PACKAGE = {SCHEMA_PACKAGE!r}",
            f"SCHEMA_VERSION = {schema_source.version!r}",
            f"SCHEMA_SHA256 = {schema_source.sha256!r}",
            f"GENERATOR_VERSION = {GENERATOR_VERSION!r}",
            "",
            "__all__ = [",
            '    "GENERATOR_VERSION",',
            '    "SCHEMA_PACKAGE",',
            '    "SCHEMA_SHA256",',
            '    "SCHEMA_URL",',
            '    "SCHEMA_VERSION",',
            "]",
        ],
    )
    return "\n".join(lines)


def render_typed_dicts(
    generator: Generator,
    order: Sequence[str],
    forward_refs: Mapping[str, set[str]],
) -> str:
    """Render generated TypedDict classes."""
    payload_dict_names = sorted({d.dict_name for d in generator.registry.values() if d.is_event_payload})
    all_dict_names = sorted({d.dict_name for d in generator.registry.values()})
    lines = generated_header("TypedDict payloads generated from Octokit's GitHub webhook schema.")
    lines.extend(
        [
            "from typing import Any, Literal, NotRequired, Required, TypedDict",
            "",
            f"__all__ = {sorted([*all_dict_names, 'WebhookPayload'])!r}",
            "",
        ],
    )
    for key in order:
        defn = generator.registry[key]
        lines.extend(render_typed_dict_class(defn, forward_refs.get(key, set())))
        lines.append("")
    lines.append(render_union_alias("WebhookPayload", payload_dict_names, fallback="dict[str, Any]"))
    return "\n".join(lines)


def render_typed_dict_class(defn: Definition, forward_dict_names: set[str]) -> list[str]:
    """Render one TypedDict (class-form if all keys are identifiers, else functional-form)."""
    has_non_identifier = any(not is_python_identifier(name) for name in defn.fields)
    if has_non_identifier:
        return render_functional_typed_dict(defn, forward_dict_names)

    lines = [f"class {defn.dict_name}(TypedDict, total=False):"]
    lines.append(f'    """{class_docstring(defn)}"""')
    if not defn.fields:
        return lines
    for field_name, spec in defn.fields.items():
        type_expr = quote_forward_refs(spec.type_expr, forward_dict_names)
        wrapper = "Required" if spec.required else "NotRequired"
        lines.append(f"    {field_name}: {wrapper}[{type_expr}]")
    return lines


def render_functional_typed_dict(defn: Definition, forward_dict_names: set[str]) -> list[str]:
    """Render a TypedDict via the functional form to support non-identifier keys."""
    lines = [f"{defn.dict_name} = TypedDict("]
    lines.append(f"    {defn.dict_name!r},")
    lines.append("    {")
    for field_name, spec in defn.fields.items():
        type_expr = quote_forward_refs(spec.type_expr, forward_dict_names)
        wrapper = "Required" if spec.required else "NotRequired"
        lines.append(f"        {field_name!r}: {wrapper}[{type_expr}],")
    lines.append("    },")
    lines.append("    total=False,")
    lines.append(")")
    lines.append(f'{defn.dict_name}.__doc__ = """{class_docstring(defn)}"""')
    return lines


def render_models(
    generator: Generator,
    order: Sequence[str],
    forward_refs: Mapping[str, set[str]],
) -> str:
    """Render generated Pydantic model classes."""
    payload_class_names = sorted({d.class_name for d in generator.registry.values() if d.is_event_payload})
    all_class_names = sorted({d.class_name for d in generator.registry.values()})
    dict_to_class = {d.dict_name: d.class_name for d in generator.registry.values()}

    lines = generated_header("Pydantic models generated from Octokit's GitHub webhook schema.")
    lines.extend(
        [
            "from typing import Any, Literal",
            "",
            "from pydantic import BaseModel, ConfigDict, Field",
            "",
            f"__all__ = {sorted([*all_class_names, 'WebhookPayloadModel'])!r}",
            "",
        ],
    )
    cyclic_classes: list[str] = []
    for key in order:
        defn = generator.registry[key]
        forward_class_names = {dict_to_class[name] for name in forward_refs.get(key, set())}
        if forward_class_names:
            cyclic_classes.append(defn.class_name)
        lines.extend(render_model_class(defn, dict_to_class, forward_class_names))
        lines.append("")
    for class_name in cyclic_classes:
        lines.append(f"{class_name}.model_rebuild()")
    if cyclic_classes:
        lines.append("")
    lines.append(render_union_alias("WebhookPayloadModel", payload_class_names, fallback="BaseModel"))
    return "\n".join(lines)


def render_model_class(
    defn: Definition,
    dict_to_class: Mapping[str, str],
    forward_class_names: set[str],
) -> list[str]:
    """Render one Pydantic class body."""
    lines = [f"class {defn.class_name}(BaseModel):"]
    lines.append(f'    """{class_docstring(defn)}"""')
    lines.append("")
    lines.append('    model_config = ConfigDict(extra="allow", populate_by_name=True)')
    if not defn.fields:
        return lines
    lines.append("")
    for field_name, spec in defn.fields.items():
        model_expr = dict_to_class_in_expr(spec.type_expr, dict_to_class)
        model_expr = quote_forward_refs(model_expr, forward_class_names)
        attr = safe_field_name(field_name)
        annotation = model_expr if spec.required else with_optional(model_expr)
        if attr != field_name:
            field_call = (
                f"Field(alias={field_name!r})" if spec.required else f"Field(default=None, alias={field_name!r})"
            )
            lines.append(f"    {attr}: {annotation} = {field_call}")
        elif spec.required:
            lines.append(f"    {attr}: {annotation}")
        else:
            lines.append(f"    {attr}: {annotation} = None")
    return lines


def simplify_union(parts: list[str]) -> list[str]:
    """Drop Literal members already subsumed by a sibling primitive (PYI051 cases).

    e.g. `Literal[""] | str` is just `str`; the upstream schema declares the literal
    alongside `string` to flag a sentinel value, but at the type level it's redundant.
    """
    has_str = "str" in parts
    has_int = "int" in parts
    out: list[str] = []
    for part in parts:
        if part.startswith("Literal[") and part.endswith("]"):
            inner_values = [v.strip() for v in part[len("Literal[") : -1].split(",")]
            if has_str and all(v.startswith(("'", '"')) for v in inner_values):
                continue
            if has_int and all(v.lstrip("-").isdigit() for v in inner_values):
                continue
        out.append(part)
    return out


def with_optional(expr: str) -> str:
    """Append `| None` to `expr` unless `None` is already a top-level union member."""
    parts = [p.strip() for p in expr.split(" | ")]
    if "None" in parts:
        return expr
    return f"{expr} | None"


def dict_to_class_in_expr(expr: str, dict_to_class: Mapping[str, str]) -> str:
    """Rewrite TypedDict-flavored annotations to reference Pydantic model classes instead."""
    pattern = re.compile(r"\b([A-Z][A-Za-z0-9]*Dict[0-9]*)\b")

    def replace(match: re.Match[str]) -> str:
        token = match.group(1)
        return dict_to_class.get(token, token)

    return pattern.sub(replace, expr)


def quote_forward_refs(expr: str, forward_names: set[str]) -> str:
    """Wrap any whole-word occurrence of a forward-referenced name in quotes."""
    if not forward_names:
        return expr
    pattern = re.compile(r"\b(" + "|".join(re.escape(name) for name in sorted(forward_names)) + r")\b")
    return pattern.sub(lambda m: f'"{m.group(1)}"', expr)


def class_docstring(defn: Definition) -> str:
    if defn.is_event_payload:
        action_suffix = f" with action `{defn.action}`." if defn.action else "."
        text = f"Payload for the GitHub `{defn.event}` webhook{action_suffix}"
    elif defn.description:
        text = defn.description
    elif defn.title:
        text = defn.title
    else:
        text = defn.class_name
    return escape_docstring(text)


def escape_docstring(text: str) -> str:
    """Normalize text for safe embedding inside `\"\"\"...\"\"\"` without escape sequences.

    Drops backslashes (rare in Octokit docs; avoiding them keeps Ruff D301 happy),
    swaps any literal `\"\"\"` to `'''` so the closing triple-quote stays unambiguous,
    strips trailing quote characters that would otherwise butt against the closer,
    and ensures terminal punctuation so Ruff D415 is satisfied.
    """
    s = text.replace("\\", "")
    s = s.replace('"""', "'''")
    s = s.rstrip()
    while s.endswith('"'):
        s = s[:-1].rstrip()
    if not s:
        return "Generated payload."
    if not s.endswith((".", "!", "?")):
        s += "."
    return s


def render_events(generator: Generator) -> str:
    """Render generated event registries."""
    payloads = [d for d in generator.registry.values() if d.is_event_payload]
    payloads.sort(key=lambda p: (p.event or "", p.action or "", p.class_name))
    event_names = sorted({p.event for p in payloads if p.event is not None})
    model_names = ", ".join(sorted({p.class_name for p in payloads}))
    fallback_by_event: OrderedDict[str, Definition] = OrderedDict()
    first_by_event: OrderedDict[str, Definition] = OrderedDict()
    for payload in payloads:
        if payload.event is None:
            continue
        first_by_event.setdefault(payload.event, payload)
        if payload.action is None:
            fallback_by_event[payload.event] = payload
    dict_names = ", ".join(sorted({p.dict_name for p in first_by_event.values()}))
    lines = generated_header("Event registries generated from Octokit's GitHub webhook schema.")
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
        if payload.action is not None and payload.event is not None:
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


def is_python_identifier(name: str) -> bool:
    """Return whether `name` can be used directly as a Python attribute / class-form key."""
    return name.isidentifier() and not keyword.iskeyword(name)


def safe_field_name(field_name: str) -> str:
    """Return a Pydantic-safe attribute name. The original key is preserved via Field(alias=...)."""
    if is_python_identifier(field_name):
        return field_name
    char_replacements = {"+": "plus", "-": "minus"}
    out = "".join(char_replacements.get(ch, ch) for ch in field_name)
    out = re.sub(r"[^0-9A-Za-z_]", "_", out)
    if not out or out[0].isdigit():
        out = f"f_{out}"
    if keyword.iskeyword(out):
        out += "_"
    return out


def clean_doc(value: str) -> str:
    """Make schema descriptions usable in one-line generated docstrings/fields."""
    return re.sub(r"\s+", " ", value).strip()


def pascal_case(value: str) -> str:
    """Convert an event/action name to PascalCase."""
    parts = re.split(r"[^A-Za-z0-9]+", value)
    return "".join(part[:1].upper() + part[1:] for part in parts if part)


def singularize(name: str) -> str:
    """Best-effort singularization for naming inline list items.

    Octokit field names are simple enough that the trailing-`s` heuristic covers
    `commits`, `reviewers`, `labels`, etc. without overreach (`status`, `address` are not
    inline-array field names in this schema).
    """
    if len(name) > 3 and name.endswith("ies"):
        return name[:-3] + "y"
    if len(name) > 1 and name.endswith("s") and not name.endswith("ss"):
        return name[:-1]
    return name


# ---------------------------------------------------------------------- IO / formatting


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
    """Return generated files after the same Ruff normalization used for writes.

    Writes into a tempdir that mirrors the project's directory layout and copies
    `pyproject.toml` so Ruff's per-file-ignores patterns (anchored to the project root)
    resolve identically to a real on-disk run.
    """
    with tempfile.TemporaryDirectory() as directory:
        temp_root = Path(directory)
        (temp_root / "pyproject.toml").write_text(
            (ROOT / "pyproject.toml").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        temp_generated = temp_root / GENERATED.relative_to(ROOT)
        temp_files: dict[Path, Path] = {}
        for path, source in files.items():
            temp_path = temp_root / path.relative_to(ROOT)
            temp_path.parent.mkdir(parents=True, exist_ok=True)
            temp_path.write_text(source, encoding="utf-8")
            temp_files[path] = temp_path

        run_ruff_on_path(temp_generated, cwd=temp_root)
        return {path: temp_path.read_text(encoding="utf-8") for path, temp_path in temp_files.items()}


def run_ruff_format() -> None:
    """Format generated files if Ruff is available."""
    run_ruff_on_path(GENERATED, cwd=ROOT)


def run_ruff_on_path(path: Path, *, cwd: Path) -> None:
    """Run Ruff's deterministic format/fix pipeline on a path."""
    subprocess.run([sys.executable, "-m", "ruff", "format", str(path)], cwd=cwd, check=True)
    subprocess.run([sys.executable, "-m", "ruff", "check", "--fix", str(path)], cwd=cwd, check=True)
    subprocess.run([sys.executable, "-m", "ruff", "format", str(path)], cwd=cwd, check=True)


if __name__ == "__main__":
    raise SystemExit(main())
