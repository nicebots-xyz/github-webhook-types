# SPDX-License-Identifier: ISC
# Copyright: 2026 NiceBots.xyz
"""Generated GitHub webhook payload types and registries."""

from github_webhook_types.generated.events import EVENT_MODEL_BY_NAME, EVENT_TYPED_DICT_BY_NAME, GitHubEventName
from github_webhook_types.generated.models import WebhookPayloadModel
from github_webhook_types.generated.typed_dicts import WebhookPayload

__all__ = [
    "EVENT_MODEL_BY_NAME",
    "EVENT_TYPED_DICT_BY_NAME",
    "GitHubEventName",
    "WebhookPayload",
    "WebhookPayloadModel",
]
