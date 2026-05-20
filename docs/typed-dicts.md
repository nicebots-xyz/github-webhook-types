<!--
SPDX-License-Identifier: ISC
Copyright: 2026 NiceBots.xyz
-->
# TypedDict Reference

Generated `TypedDict` payload classes are the canonical reference for webhook payload fields.

!!! note
    Every generated `TypedDict` payload is also available as a Pydantic model with the same base name.
    For example, `IssuesOpenedPayloadDict` is available as `IssuesOpenedPayload` from
    `github_webhook_types.generated.models`.

    Pydantic models are built from these generated `TypedDict` definitions at runtime and allow unknown
    extra fields, matching GitHub's ability to add webhook fields over time.

::: github_webhook_types.generated.typed_dicts
    options:
      show_submodules: false
      show_source: false
