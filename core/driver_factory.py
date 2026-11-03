"""Driver factory for Appium and Playwright automation."""

from __future__ import annotations

from typing import Any

from appium import webdriver as appium_webdriver
from playwright.sync_api import sync_playwright


class DriverFactory:
    """Create browser or mobile drivers with explicit configuration."""

    @staticmethod
    def create_appium_driver(desired_caps: dict[str, Any]) -> Any:
        return appium_webdriver.Remote("http://127.0.0.1:4723", desired_caps)

    @staticmethod
    def create_playwright_browser(headless: bool = True, browser_name: str = "chromium") -> Any:
        playwright = sync_playwright().start()
        browser = getattr(playwright, browser_name).launch(headless=headless)
        return browser
