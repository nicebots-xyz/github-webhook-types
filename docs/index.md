<!--
SPDX-License-Identifier: ISC
Copyright: 2026 NiceBots.xyz
-->
# github-webhook-types

`github-webhook-types` provides generated Python types for GitHub webhook payloads.

The generated modules are built from Octokit's machine-readable webhook schema. The repository commits generated Python code and source metadata, but it does not vendor the Octokit schema JSON.

## Install

```bash
pip install github-webhook-types
```

## Quick Example

```python
from github_webhook_types import parse_delivery

payload = parse_delivery("issues", b'{"action": "opened", "repository": {}, "sender": {}, "issue": {}}')
```
