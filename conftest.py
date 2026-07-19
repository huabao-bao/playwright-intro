import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    """每个测试函数自动获得一个干净的浏览器页面"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = True)
        page_obj = browser.new_page()
        yield page_obj
        browser.close()