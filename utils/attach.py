import allure
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(png, 'screenshot', AttachmentType.PNG, '.png')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'html', AttachmentType.HTML, '.html')


def add_logs(browser):
    log = ''.join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'logs', AttachmentType.TEXT, '.log')