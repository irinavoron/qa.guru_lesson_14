from selene import browser

from tests.conftest import desktop_only, mobile_only

"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""


@desktop_only
def test_github_desktop(browser_settings):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()


@mobile_only
def test_github_mobile(browser_settings):
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
