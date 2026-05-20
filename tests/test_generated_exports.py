# SPDX-License-Identifier: ISC
# Copyright: 2026 NiceBots.xyz
from github_webhook_types import generated
from github_webhook_types.generated import events, models, typed_dicts


def test_generated_exports_exist() -> None:
    for module in (generated, events, models, typed_dicts):
        assert module.__all__
        for name in module.__all__:
            assert hasattr(module, name)


def test_generated_registries_are_non_empty() -> None:
    assert events.EVENT_MODEL_BY_NAME
    assert events.EVENT_MODEL_BY_NAME_AND_ACTION
    assert events.EVENT_TYPED_DICT_BY_NAME
    assert "push" in events.EVENT_MODEL_BY_NAME
    assert ("issues", "opened") in events.EVENT_MODEL_BY_NAME_AND_ACTION
