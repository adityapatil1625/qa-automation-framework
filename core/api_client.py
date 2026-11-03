"""Thin API wrapper for REST requests with timeout and JSON validation hooks."""

from __future__ import annotations

from typing import Any

import requests


class ApiClient:
    """Simple wrapper around requests for REST testing."""

    def __init__(self, base_url: str, timeout: int = 15) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def get(self, path: str, **kwargs: Any) -> requests.Response:
        return requests.get(f"{self.base_url}/{path.lstrip('/')}", timeout=self.timeout, **kwargs)

    def post(self, path: str, **kwargs: Any) -> requests.Response:
        return requests.post(f"{self.base_url}/{path.lstrip('/')}", timeout=self.timeout, **kwargs)

    def put(self, path: str, **kwargs: Any) -> requests.Response:
        return requests.put(f"{self.base_url}/{path.lstrip('/')}", timeout=self.timeout, **kwargs)

    def delete(self, path: str, **kwargs: Any) -> requests.Response:
        return requests.delete(f"{self.base_url}/{path.lstrip('/')}", timeout=self.timeout, **kwargs)
