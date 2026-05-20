# SPDX-License-Identifier: ISC
# Copyright: 2026 NiceBots.xyz
import pytest
from pydantic import ValidationError

from github_webhook_types import UnknownWebhookEventError, parse_delivery
from github_webhook_types.generated.models import IssuesOpenedPayload, PushPayload


def test_parse_delivery_dispatches_event_payload() -> None:
    payload = parse_delivery(
        "push",
        (
            b'{"after": "b", "base_ref": null, "before": "a", "commits": [], '
            b'"compare": "https://github.com/octo/repo/compare/a...b", "created": false, '
            b'"deleted": false, "forced": false, "head_commit": null, "pusher": {}, '
            b'"ref": "refs/heads/master", "repository": {}, "sender": {}}'
        ),
    )
    assert isinstance(payload, PushPayload)


def test_parse_delivery_dispatches_action_payload() -> None:
    payload = parse_delivery(
        "issues",
        {
            "action": "opened",
            "issue": {},
            "repository": {},
            "sender": {},
        },
    )
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
