"""Application configuration management for local and CI execution."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Centralized runtime configuration with sensible defaults."""

    def __init__(self, config_path: str | Path | None = None) -> None:
        self.config_path = Path(config_path) if config_path else Path(__file__).resolve().parents[1] / "config.yaml"
        self._data: dict[str, Any] = {}
        self.reload()

    def reload(self) -> None:
        """Load YAML config and overlay environment variables for runtime overrides."""
        if self.config_path.exists():
            with self.config_path.open("r", encoding="utf-8") as handle:
                self._data = yaml.safe_load(handle) or {}
        else:
            self._data = {}

    def get(self, key: str, default: Any = None) -> Any:
        """Fetch a nested config value using dot notation."""
        current: Any = self._data
        for part in key.split("."):
            if not isinstance(current, dict) or part not in current:
                return os.getenv(key.upper().replace(".", "_"), default)
            current = current[part]
        return current


settings = Settings()
