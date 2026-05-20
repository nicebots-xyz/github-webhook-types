# SPDX-License-Identifier: ISC
# Copyright: 2026 NiceBots.xyz
"""Package-specific errors."""


class UnknownWebhookEventError(ValueError):
    """Raised when no generated model is available for a GitHub webhook event."""


class UnknownWebhookActionError(ValueError):
    """Raised when no generated model is available for a GitHub webhook action."""
