"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser

desktop_only = pytest.mark.parametrize(
    argnames='browser_settings',
    argvalues=[(1920, 1080), (1366, 768), (1536, 864)],
    ids=['large', 'medium', 'small'],
    indirect=True
)

mobile_only = pytest.mark.parametrize(
    argnames='browser_settings',
    argvalues=[(360, 780), (390, 844), (414, 896)],
    ids=['iPhone 12 mini', 'iPhone 12 Pro', 'iPhone XR'],
    indirect=True
)


@desktop_only
def test_github_desktop(browser_settings):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()


@mobile_only
def test_github_mobile(browser_settings):
    browser.open('/')
    browser.element('.Button-content').click()
    browser.element('.HeaderMenu-link--sign-in').click()
