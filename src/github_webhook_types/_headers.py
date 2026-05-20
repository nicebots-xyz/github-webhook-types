# SPDX-License-Identifier: ISC
# Copyright: 2026 NiceBots.xyz
"""Typed GitHub webhook delivery headers."""

from typing import NotRequired, Required, TypedDict


class DeliveryHeaders(TypedDict, total=False):
    """Relevant GitHub webhook delivery headers normalized to Python keys."""

    event: Required[str]
    delivery: Required[str]
    signature_256: NotRequired[str]
    hook_id: NotRequired[str]
