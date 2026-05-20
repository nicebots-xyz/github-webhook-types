<!--
SPDX-License-Identifier: ISC
Copyright: 2026 NiceBots.xyz
-->
# Delivery Headers

GitHub webhook payload shape is selected by `X-GitHub-Event`.

Common headers:

- `X-GitHub-Event`: event name, such as `push` or `issues`
- `X-GitHub-Delivery`: delivery identifier
- `X-Hub-Signature-256`: HMAC signature using SHA-256
- `X-GitHub-Hook-ID`: hook identifier

`DeliveryHeaders` is a small `TypedDict` for normalized versions of those headers.

!!! note
    `parse_delivery()` expects the normalized event name, usually the value of `X-GitHub-Event`.
    Signature verification is intentionally outside this package's scope.
