<!--
SPDX-License-Identifier: ISC
Copyright: 2026 NiceBots.xyz
-->
# Usage

Import concrete payload `TypedDict` types from the generated module.

```python
from github_webhook_types.generated.typed_dicts import IssuesOpenedPayloadDict

payload: IssuesOpenedPayloadDict = {
    "action": "opened",
    "repository": {},
    "sender": {},
    "issue": {},
}
```

The same payload is available as a Pydantic model by removing the `Dict` suffix.

```python
from github_webhook_types.generated.models import IssuesOpenedPayload

model = IssuesOpenedPayload.model_validate(payload)
```

Use `parse_delivery` when handling webhook deliveries dynamically.

```python
from github_webhook_types import parse_delivery

model = parse_delivery("push", request_body)
```

Generated Pydantic models mirror the generated `TypedDict` definitions field-for-field and allow unknown
extra fields because GitHub can add payload fields over time.

!!! note
    The `TypedDict` reference is the canonical field reference. Pydantic model names use the same payload name
    without the `Dict` suffix.
