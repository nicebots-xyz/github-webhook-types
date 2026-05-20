# SPDX-License-Identifier: ISC
# Copyright: 2026 NiceBots.xyz
"""Runtime payload validation helpers."""

import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, cast

from github_webhook_types._errors import UnknownWebhookActionError, UnknownWebhookEventError
from github_webhook_types.generated.events import (
    EVENT_ACTIONS_BY_NAME,
    EVENT_MODEL_BY_NAME,
    EVENT_MODEL_BY_NAME_AND_ACTION,
)

if TYPE_CHECKING:
    from github_webhook_types.generated.models import WebhookPayloadModel


def parse_delivery(event: str, payload: bytes | str | Mapping[str, object]) -> "WebhookPayloadModel":
    """Validate a GitHub webhook delivery payload for the given event name."""
    payload_data = _coerce_payload(payload)
    action = payload_data.get("action")
    model_type = None

    if isinstance(action, str):
        model_type = EVENT_MODEL_BY_NAME_AND_ACTION.get((event, action))
        if model_type is None and event in EVENT_ACTIONS_BY_NAME and event not in EVENT_MODEL_BY_NAME:
            msg = f"No generated GitHub webhook model is registered for event {event!r} with action {action!r}."
            raise UnknownWebhookActionError(msg)

    if model_type is None:
        model_type = EVENT_MODEL_BY_NAME.get(event)

    if model_type is None:
        if event in EVENT_ACTIONS_BY_NAME:
            msg = f"No generated GitHub webhook model is registered for event {event!r} without a supported action."
            raise UnknownWebhookActionError(msg)
        msg = f"No generated GitHub webhook model is registered for event {event!r}."
        raise UnknownWebhookEventError(msg)

    return model_type.model_validate(payload_data)


def _coerce_payload(payload: bytes | str | Mapping[str, object]) -> Mapping[str, Any]:
    if isinstance(payload, bytes):
        loaded = json.loads(payload.decode())
    elif isinstance(payload, str):
        loaded = json.loads(payload)
    else:
        return payload

    if not isinstance(loaded, dict):
        msg = "GitHub webhook payload must decode to a JSON object."
        raise TypeError(msg)

    return cast("Mapping[str, Any]", loaded)
