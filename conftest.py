import pytest
from playwright.sync_api import sync_playwright
from config.settings import HEADLESS

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()