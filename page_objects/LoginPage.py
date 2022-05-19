from selenium.webdriver.common.by import By
from page_objects.Actions import Actions


class LoginPage(Actions):
    ACC_DROPDOWN = (By.CSS_SELECTOR, ".caret")
    REGISTER_BUTTON = (By.XPATH, "//li[@class='dropdown open']/ul/li[1]")
    LOGIN_BUTTON = (By.XPATH, "//li[@class='dropdown open']/ul/li[2]")
    CONTINUE_TO_REGISTER = (By.LINK_TEXT, "Continue")
    LOGIN = (By.XPATH, "//input[@value='Login']")
    EMAIL = (By.CSS_SELECTOR, "#input-email")
    PASS = (By.CSS_SELECTOR, "#input-password")

    def click_dropdown(self):
        self._click(self.ACC_DROPDOWN)

    def click_login(self):
        self.click_dropdown()
        self._click(self.LOGIN_BUTTON)
        return self

    def continue_to_register(self):
        self._click(self.CONTINUE_TO_REGISTER)

    def login(self):
        with open("data.txt", "r") as file:
            email, password = file.read().split("\n")
        self._send_keys(self.EMAIL, email)
        self._send_keys(self.PASS, password)
        self._click(self.LOGIN)

    def inners(self):
        self._element((By.LINK_TEXT, "Edit your account information"))
        self._element((By.LINK_TEXT, "Change your password"))

    def change_password(self):
        new_password = "00000"
        self._click((By.LINK_TEXT, "Change your password"))
        self._send_keys((By.CSS_SELECTOR, "#input-password"), new_password)
        self._send_keys((By.CSS_SELECTOR, "#input-confirm"), new_password)
