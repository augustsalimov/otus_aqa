import logging
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Actions:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 3)
        self.__config_logger()

    def __config_logger(self):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.addHandler(logging.FileHandler(f"logs/{self.browser.test_name}.log"))
        self.logger.setLevel(level=self.browser.log_level)

    def _verify_link_presence(self, link_text):
        try:
            return WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
        except TimeoutException:
            raise AssertionError("Cant find element by link text: {}".format(link_text))

    def _verify_element_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def _element(self, locator: tuple):
        self.logger.info("Returning element {}".format(locator))
        return self._verify_element_presence(locator)

    def _click(self, locator):
        self.logger.info("Clicking element {}".format(locator))
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    def _click_link(self, link_text):
        self.logger.info("Clicking link {}".format(link_text))
        self._click((By.LINK_TEXT, link_text))

    def _send_keys(self, locator: tuple, text: str):
        self.logger.info("Input {} in {} locator".format(text, locator))
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)
