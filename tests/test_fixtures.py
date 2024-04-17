"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import allure
from selene import browser


def test_github_desktop(desktop_browser_settings):
    with allure.step('Open main page'):
        browser.open('/')
    with allure.step('Open the SignIn form'):
        browser.element('.HeaderMenu-link--sign-in').click()


def test_github_mobile(mobile_browser_settings):
    with allure.step('Open main page'):
        browser.open('/')
    with allure.step('Open the SignIn form'):
        browser.element('.Button-content').click()
        browser.element('.HeaderMenu-link--sign-in').click()
