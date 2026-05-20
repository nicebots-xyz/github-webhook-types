# SPDX-License-Identifier: ISC
# Copyright: 2026 NiceBots.xyz
from pathlib import Path

import github_webhook_types


def test_package_exports() -> None:
    assert github_webhook_types.DeliveryHeaders
    assert github_webhook_types.GitHubEventName
    assert github_webhook_types.WebhookPayload
    assert github_webhook_types.WebhookPayloadModel
    assert github_webhook_types.UnknownWebhookEventError
    assert github_webhook_types.UnknownWebhookActionError
    assert github_webhook_types.parse_delivery


def test_py_typed_exists() -> None:
    package_root = Path(github_webhook_types.__file__).parent
    assert (package_root / "py.typed").exists()
