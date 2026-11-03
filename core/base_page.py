"""Reusable base classes for page objects and explicit waiting."""

from __future__ import annotations

from abc import ABC

from playwright.sync_api import Page, expect


class BaseWebPage(ABC):
    """Base page object for Playwright flows with explicit waiting."""

    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self, url: str) -> None:
        self.page.goto(url)

    def wait_for_url(self, expected_substring: str) -> None:
        expect(self.page).to_have_url(f"*{expected_substring}*")


class BaseMobilePage(ABC):
    """Base page object for Appium mobile flows."""

    def __init__(self, driver: object) -> None:
        self.driver = driver
