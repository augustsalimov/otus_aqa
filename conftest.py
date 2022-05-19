import os
import pytest
import logging
from datetime import datetime
from selenium import webdriver

DRIVERS = os.path.expanduser("~/drivers")


def pytest_addoption(parser):
    parser.addoption("--browser", default="ff")
    parser.addoption("--url", default="https://demo.opencart.com")
    parser.addoption("--log_level", default="DEBUG")


@pytest.fixture(autouse=True)
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger('driver')
    test_name = request.node.name

    logger.addHandler(logging.FileHandler(f"logs/{test_name}.log"))
    logger.setLevel(level=log_level)

    logger.info("==> Test {} started at {}".format(test_name, datetime.now()))

    if url == 'local':
        caps = {'goog:chromeOptions': {}}
        driver = webdriver.Chrome(desired_capabilities=caps)
    else:
        caps = {
            "browserName": browser,
            "screenResolution": "1280x720",
            "selenoid:options": {
                "enableVNC": True,
            },
            "goog:chromeOptions": {}
        }
        driver = webdriver.Remote(
            command_executor=url,
            desired_capabilities=caps
        )
        driver.maximize_window()

    driver.test_name = test_name
    driver.log_level = log_level
    logger.info("Browser: {}".format(browser, driver.capabilities))

    def fin():
        driver.quit()
        logger.info("==> Test {} finished at {}".format(test_name, datetime.now()))

    request.addfinalizer(fin)
    return driver
