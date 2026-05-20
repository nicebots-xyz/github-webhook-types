# SPDX-License-Identifier: ISC
# Copyright: 2026 NiceBots.xyz
"""Helpers for building runtime payload models from generated TypedDicts."""

from typing import Any, NotRequired, Required, cast, get_args, get_origin, get_type_hints

from pydantic import BaseModel, ConfigDict, create_model


def build_model_from_typeddict(model_name: str, typed_dict: type, *, doc: str) -> type[BaseModel]:
    """Create a Pydantic model class from a generated TypedDict class."""
    hints = get_type_hints(typed_dict, include_extras=True)
    required_keys = cast("frozenset[str]", getattr(typed_dict, "__required_keys__", frozenset[str]()))
    fields: dict[str, Any] = {}

    for field_name, annotation in hints.items():
        field_type = _strip_required_marker(annotation)
        if field_name in required_keys:
            fields[field_name] = (field_type, ...)
        else:
            fields[field_name] = (_nullable(field_type), None)

    return create_model(
        model_name,
        __config__=ConfigDict(extra="allow"),
        __doc__=doc,
        __module__="github_webhook_types.generated.models",
        **fields,
    )


def _strip_required_marker(annotation: object) -> object:
    origin = get_origin(annotation)
    if origin in {Required, NotRequired}:
        args = get_args(annotation)
        return args[0] if args else Any
    return annotation


def _nullable(annotation: object) -> object:
    if annotation is Any:
        return Any
    args = get_args(annotation)
    if type(None) in args:
        return annotation
    return cast("Any", annotation) | None
