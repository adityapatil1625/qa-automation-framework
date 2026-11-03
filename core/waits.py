"""Reusable explicit wait helpers for browser and mobile actions."""

from __future__ import annotations

from typing import Any

from playwright.sync_api import Page, expect


def wait_for_element(page: Page, selector: str, timeout: int = 15000) -> None:
    """Wait for a selector to be visible without using sleep."""
    expect(page.locator(selector)).to_be_visible(timeout=timeout)


def wait_for_text(page: Page, text: str, timeout: int = 15000) -> None:
    """Wait for visible text content on the page."""
    expect(page.get_by_text(text)).to_be_visible(timeout=timeout)


def wait_for_mobile_condition(driver: Any, condition: str, timeout_ms: int = 15000) -> None:
    """Placeholder explicit wait for Appium condition checks."""
    driver.implicitly_wait(timeout_ms / 1000)
