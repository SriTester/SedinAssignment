from allure_commons.types import AttachmentType
import allure
import pytest
from Base.Base import WebDriverClass

@pytest.fixture(scope = 'class')
def startdriver (request):
    session = WebDriverClass()
    driver = session.getchromedriver()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture(scope = 'function')
def log_on_failure (request, startdriver):
    yield
    driver = startdriver
    item = request.node
    if item.rep_call.failed:
        allure.attach ( driver.get_screenshot_as_png(), name = 'Screen_Shot', attachment_type = AttachmentType.PNG )
        driver.quit()

