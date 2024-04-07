"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser


def test_github_desktop(browser_settings):
    if browser_settings == 'mobile':
        pytest.skip('This is mobile resolution')
    else:
        browser.open('/')
        browser.element('.HeaderMenu-link--sign-in').click()


def test_github_mobile(browser_settings):
    if browser_settings == 'desktop':
        pytest.skip('This is desktop resolution')
    else:
        browser.open('/')
        browser.element('.Button-content').click()
        browser.element('.HeaderMenu-link--sign-in').click()
