# SPDX-License-Identifier: ISC
# Copyright: 2026 NiceBots.xyz
import json
from pathlib import Path

import pytest
from pydantic import ValidationError

from github_webhook_types import UnknownWebhookEventError, parse_delivery
from github_webhook_types.generated.models import IssuesOpenedPayload, PushPayload

FIXTURES = Path(__file__).parent / "fixtures"


def test_parse_delivery_dispatches_event_payload() -> None:
    body = (FIXTURES / "push.json").read_bytes()
    payload = parse_delivery("push", body)
    assert isinstance(payload, PushPayload)


def test_parse_delivery_dispatches_action_payload() -> None:
    payload = parse_delivery("issues", json.loads((FIXTURES / "issues.opened.json").read_text(encoding="utf-8")))
    assert isinstance(payload, IssuesOpenedPayload)


def test_parse_delivery_unknown_event() -> None:
    with pytest.raises(UnknownWebhookEventError):
        parse_delivery("missing", {})


def test_parse_delivery_invalid_json_object() -> None:
    with pytest.raises(TypeError):
        parse_delivery("push", "[]")


def test_parse_delivery_validation_failure() -> None:
    with pytest.raises(ValidationError):
        parse_delivery("push", {})
