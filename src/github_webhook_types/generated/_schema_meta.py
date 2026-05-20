# SPDX-License-Identifier: ISC
# Copyright: 2026 NiceBots.xyz
"""Octokit schema metadata used for the generated payload types."""

SCHEMA_URL = "https://unpkg.com/@octokit/webhooks-schemas/schema.json"
EXAMPLES_URL = "https://unpkg.com/@octokit/webhooks-examples/api.github.com/index.json"
SCHEMA_PACKAGE = "@octokit/webhooks-schemas"
EXAMPLES_PACKAGE = "@octokit/webhooks-examples"
SCHEMA_VERSION = "7.6.1"
EXAMPLES_VERSION = "7.6.1"
SCHEMA_SHA256 = "ff15ae017ba3b877a44f636806155f986f7b707b31aa7eebde6da1d3366f2840"
EXAMPLES_SHA256 = "09d8f0c617876ae9dad22e26fea5510bfcaad50ee7e602659f6db25b87b25815"
GENERATOR_VERSION = "0.1.0"

__all__ = [
    "EXAMPLES_PACKAGE",
    "EXAMPLES_SHA256",
    "EXAMPLES_URL",
    "EXAMPLES_VERSION",
    "GENERATOR_VERSION",
    "SCHEMA_PACKAGE",
    "SCHEMA_SHA256",
    "SCHEMA_URL",
    "SCHEMA_VERSION",
]
