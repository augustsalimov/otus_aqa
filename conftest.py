import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service

DRIVERS = os.path.expanduser("~/drivers")


def pytest_addoption(parser):
    parser.addoption("--browser", default="ff")


def driver_factory(browser):
    if browser == 'ff':
        service = Service(executable_path=os.path.join(DRIVERS, "geckodriver"))
        driver = webdriver.Firefox(service=service)
    elif browser == 'chrome':
        service = Service(executable_path=os.path.join(DRIVERS, "chromedriver"))
        driver = webdriver.Chrome(service=service)
    elif browser == 'opera':
        driver = webdriver.Opera(executable_path=f"{DRIVERS}/operadriver")
    else:
        raise Exception("Driver not supported")
    return driver


@pytest.fixture(autouse=True)
def browser(request):
    driver = driver_factory(request.config.getoption("--browser"))
    request.addfinalizer(driver.quit)
    return driver
