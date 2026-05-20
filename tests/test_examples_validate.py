# SPDX-License-Identifier: ISC
# Copyright: 2026 NiceBots.xyz
from github_webhook_types.generated.models import (
    IssuesOpenedPayload,
    PingPayload,
    PullRequestOpenedPayload,
    PushPayload,
    WorkflowRunCompletedPayload,
)


def test_representative_payload_models_validate() -> None:
    assert PingPayload.model_validate(
        {
            "hook": {},
            "hook_id": 1,
            "sender": {},
            "zen": "Keep it logically awesome.",
        },
    )
    assert PushPayload.model_validate(
        {
            "after": "b",
            "base_ref": None,
            "before": "a",
            "commits": [],
            "compare": "https://github.com/octo/repo/compare/a...b",
            "created": False,
            "deleted": False,
            "forced": False,
            "head_commit": None,
            "pusher": {},
            "ref": "refs/heads/master",
            "repository": {},
            "sender": {},
        },
    )
    assert IssuesOpenedPayload.model_validate(
        {
            "action": "opened",
            "issue": {},
            "repository": {},
            "sender": {},
        },
    )
    assert PullRequestOpenedPayload.model_validate(
        {
            "action": "opened",
            "number": 1,
            "pull_request": {},
            "repository": {},
            "sender": {},
        },
    )
    assert WorkflowRunCompletedPayload.model_validate(
        {
            "action": "completed",
            "repository": {},
            "sender": {},
            "workflow": {},
            "workflow_run": {},
        },
    )
