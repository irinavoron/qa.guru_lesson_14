import os
import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

base_url = 'https://github.com/'


@pytest.fixture(autouse=True)
def selenoid_browser_settings():
    load_dotenv()

    options = Options()

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "122.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True

        }
    }

    options.capabilities.update(selenoid_capabilities)

    url = os.getenv('SELENOID_URL')
    login = os.getenv('SELENOID_LOGIN')
    password = os.getenv('SELENOID_PASSWORD')

    driver = webdriver.Remote(
        command_executor=f'https://{login}:{password}@{url}/wd/hub',
        options=options)

    browser.config.driver = driver


@pytest.fixture(
    params=[(1920, 1080), (1366, 768), (1536, 864)],
    ids=['large', 'medium', 'small']
)
def desktop_browser_settings(request):
    browser.config.base_url = base_url
    window_width, window_height = request.param
    browser.config.window_width = window_width
    browser.config.window_height = window_height

    yield

    browser.quit()


@pytest.fixture(
    params=[(360, 780), (390, 844), (414, 896)],
    ids=['iPhone 12 mini', 'iPhone 12 Pro', 'iPhone XR']
)
def mobile_browser_settings(request):
    browser.config.base_url = base_url
    window_width, window_height = request.param
    browser.config.window_width = window_width
    browser.config.window_height = window_height

    yield

    browser.quit()


@pytest.fixture(
    params=[(1920, 1080), (1366, 768), (1536, 864), (360, 780), (390, 844), (414, 896)],
    ids=['large', 'medium', 'small', 'iPhone 12 mini', 'iPhone 12 Pro', 'iPhone XR']
)
def browser_settings(request):
    browser.config.base_url = base_url
    window_width, window_height = request.param
    browser.config.window_width = window_width
    browser.config.window_height = window_height

    if window_width < 800:
        yield 'mobile'
    else:
        yield 'desktop'

    browser.quit()
