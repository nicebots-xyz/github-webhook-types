# SPDX-License-Identifier: ISC
# Copyright: 2026 NiceBots.xyz
from github_webhook_types.generated import _schema_meta


def test_schema_metadata_is_present() -> None:
    assert _schema_meta.SCHEMA_URL
    assert _schema_meta.EXAMPLES_URL
    assert _schema_meta.SCHEMA_PACKAGE == "@octokit/webhooks-schemas"
    assert _schema_meta.EXAMPLES_PACKAGE == "@octokit/webhooks-examples"
    assert _schema_meta.GENERATOR_VERSION
