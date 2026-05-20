# SPDX-License-Identifier: ISC
# Copyright: 2026 NiceBots.xyz
import json
from pathlib import Path

import pytest

from github_webhook_types.generated.models import (
    IssuesOpenedPayload,
    PingPayload,
    PullRequestOpenedPayload,
    PushPayload,
    WorkflowRunCompletedPayload,
)

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.mark.parametrize(
    ("fixture", "model"),
    [
        ("ping.json", PingPayload),
        ("push.json", PushPayload),
        ("issues.opened.json", IssuesOpenedPayload),
        ("pull_request.opened.json", PullRequestOpenedPayload),
        ("workflow_run.completed.json", WorkflowRunCompletedPayload),
    ],
)
def test_representative_payload_models_validate(fixture: str, model: type) -> None:
    payload = json.loads((FIXTURES / fixture).read_text(encoding="utf-8"))
    model.model_validate(payload)
