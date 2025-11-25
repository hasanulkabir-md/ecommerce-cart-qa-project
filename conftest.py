import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    """Simple Playwright page fixture without pytest-playwright plugin."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # change to False if you want to see browser
        page = browser.new_page()
        yield page
        browser.close()
