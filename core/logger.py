"""Central logging helper for tests and runtime tooling."""

from __future__ import annotations

import logging
import sys
from pathlib import Path


class AppLogger:
    """Create a consistent logger across the project."""

    def __init__(self, name: str = "qa_automation_framework", level: str = "INFO") -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level.upper())
        self.logger.propagate = False

        if not self.logger.handlers:
            formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
            stream_handler = logging.StreamHandler(sys.stdout)
            stream_handler.setFormatter(formatter)
            self.logger.addHandler(stream_handler)

            log_dir = Path(__file__).resolve().parents[1] / "reports"
            log_dir.mkdir(exist_ok=True)
            file_handler = logging.FileHandler(log_dir / "qa_framework.log", encoding="utf-8")
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def get_logger(self) -> logging.Logger:
        """Return the configured logger instance."""
        return self.logger


logger = AppLogger().get_logger()
