"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser


@pytest.fixture(params=[(1920, 1080), (1366, 768), (1536, 864), (360, 780), (390, 844), (414, 896)],
                ids=['large', 'medium', 'small', 'iPhone 12 mini', 'iPhone 12 Pro', 'iPhone XR'])
def browser_settings(request):
    browser.config.base_url = 'https://github.com'
    window_width, window_height = request.param
    browser.config.window_width = window_width
    browser.config.window_height = window_height


@pytest.mark.parametrize('browser_settings', [(1920, 1080), (1366, 768), (1536, 864)],
                         ids=['large', 'medium', 'small'],
                         indirect=True)
def test_github_desktop(browser_settings):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize('browser_settings', [(360, 780), (390, 844), (414, 896)],
                         ids=['iPhone 12 mini', 'iPhone 12 Pro', 'iPhone XR'],
                         indirect=True)
def test_github_mobile(browser_settings):
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
