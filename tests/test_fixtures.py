"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
from selene import browser


def test_github_desktop(desktop_browser_settings):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_github_mobile(mobile_browser_settings):
    browser.open('/')
    browser.element('.Button-content').click()
    browser.element('.HeaderMenu-link--sign-in').click()
