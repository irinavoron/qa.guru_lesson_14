import pytest
from selene import browser


@pytest.fixture(params=[(1920, 1080), (1366, 768), (1536, 864)], ids=['large', 'medium', 'small'])
def desktop(request):
    browser.config.base_url = 'https://github.com'
    window_width, window_height = request.param
    browser.config.window_width = window_width
    browser.config.window_height = window_height


@pytest.fixture(params=[(360, 780), (390, 844), (414, 896)], ids=['iPhone 12 mini', 'iPhone 12 Pro', 'iPhone XR'])
def mobile(request):
    browser.config.base_url = 'https://github.com'
    window_width, window_height = request.param
    browser.config.window_width = window_width
    browser.config.window_height = window_height
