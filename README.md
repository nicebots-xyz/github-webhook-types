<!--
SPDX-License-Identifier: ISC
Copyright: 2026 NiceBots.xyz
-->
# github-webhook-types

TypedDict definitions and Pydantic models for GitHub webhook payloads.

The package generates its public payload types from Octokit's machine-readable webhook schema. The schema JSON is not vendored in this repository; generated metadata records the upstream package versions and SHA256 hashes used to create the committed Python modules.

## Install

```bash
pip install github-webhook-types
```

## Usage

```python
from github_webhook_types import GitHubEventName, parse_delivery
from github_webhook_types.generated.models import IssuesOpenedPayload
from github_webhook_types.generated.typed_dicts import IssuesOpenedPayloadDict

event: GitHubEventName = "issues"
payload = parse_delivery(event, b'{"action": "opened", "repository": {}, "sender": {}, "issue": {}}')

typed_payload: IssuesOpenedPayloadDict = {
    "action": "opened",
    "repository": {},
    "sender": {},
    "issue": {},
}
model = IssuesOpenedPayload.model_validate(typed_payload)
```

`parse_delivery()` dispatches by `X-GitHub-Event` and, when present, the payload `action`. Unknown GitHub fields are accepted by the generated Pydantic models so new fields do not immediately break consumers.

## Type Source

Generated payload types come from:

- `https://unpkg.com/@octokit/webhooks-schemas/schema.json`
- `https://unpkg.com/@octokit/webhooks-examples/api.github.com/index.json`

The current source metadata is exported from `github_webhook_types.generated._schema_meta`.

## Development

```bash
pdm install
pdm run generate
pdm run quality
pdm run docs:build
pdm run docs:preview
pdm run docs:dev
```

Use `pdm run generate:check` to verify that the committed generated files still match the current Octokit schema metadata.
Use `pdm run docs:preview` to serve the built `site/` directory, and `pdm run docs:dev` for Zensical's live docs server.

## License

ISC.
