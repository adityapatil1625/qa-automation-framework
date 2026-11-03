"""Global pytest fixtures, markers, and screenshots-on-failure hooks."""

from __future__ import annotations

from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def playwright_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call, __multicall__):
    report = __multicall__.execute()
    if report.when == "call" and report.failed:
        screenshot_dir = Path("reports") / "screenshots"
        screenshot_dir.mkdir(parents=True, exist_ok=True)
        try:
            browser = item.funcargs.get("playwright_browser")
            if browser is not None:
                page = browser.new_page()
                page.screenshot(path=str(screenshot_dir / f"{item.name}.png"), full_page=True)
                page.close()
        except Exception:
            pass
    return report
