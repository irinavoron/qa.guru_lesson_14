"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
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

    if window_width < 900:
        yield 'mobile'
    else:
        yield 'desktop'

    browser.quit()


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
        browser.element('.Button--link').click()
        browser.element('.HeaderMenu-link--sign-in').click()
