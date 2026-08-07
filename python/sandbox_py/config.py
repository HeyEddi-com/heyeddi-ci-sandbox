"""Load shared/config.json for Python callers."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parents[2]
_CONFIG_PATH = _REPO_ROOT / "shared" / "config.json"


def load_shared_config(path: Path | None = None) -> dict[str, Any]:
    """Read and validate the shared sandbox config."""
    cfg_path = path or _CONFIG_PATH
    data = json.loads(cfg_path.read_text(encoding="utf-8"))
    for key in ("app_name", "version", "greeting"):
        if key not in data:
            raise KeyError(f"shared config missing {key!r}")
    return data
