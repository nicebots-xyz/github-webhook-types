# SPDX-License-Identifier: ISC
# Copyright: 2026 NiceBots.xyz
"""Check that generated webhook type modules are fresh."""

from scripts.generate_webhook_types import main

if __name__ == "__main__":
    raise SystemExit(main())
