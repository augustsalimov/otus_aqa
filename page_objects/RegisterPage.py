from selenium.webdriver.common.by import By
from page_objects.Actions import Actions
from helpers import random_email, random_string


class RegisterPage(Actions):
    ACC_DROPDOWN = (By.CSS_SELECTOR, ".caret")
    REGISTER_BUTTON = (By.XPATH, "//li[@class='dropdown open']/ul/li[1]")
    LOGIN_BUTTON = (By.XPATH, "//li[@class='dropdown open']/ul/li[2]")
    LOGIN_PAGE = (By.LINK_TEXT, "login page")
    PRIVACY_POLICY = (By.LINK_TEXT, "Privacy Policy")
    FIRST_NAME = (By.CSS_SELECTOR, "#input-firstname")
    LAST_NAME = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL = (By.CSS_SELECTOR, "#input-email")
    PHONE = (By.CSS_SELECTOR, "#input-telephone")
    PASS = (By.CSS_SELECTOR, "#input-password")
    CONFIRM_PASS = (By.CSS_SELECTOR, "#input-confirm")
    AGREE = (By.NAME, "agree")
    CONTINUE = (By.XPATH, "//input[@value='Continue']")
    SUCCESSFUL_ALERT = (By.XPATH, "//h1[text()='Your Account Has Been Created!']")
    ALERT = (By.CSS_SELECTOR, ".alert-danger")

    def click_dropdown(self):
        self._simple_click(self.ACC_DROPDOWN)

    def click_register(self):
        self.click_dropdown()
        self._simple_click(self.REGISTER_BUTTON)

    def click_all_elements_of_right_menu(self):
        for i in range(1, 14):
            self._simple_click((By.XPATH, f"//div[@class='list-group']/a[{i}]"))

    def click_login(self):
        self.click_dropdown()
        self._simple_click(self.LOGIN_BUTTON)

    def go_to_login_page(self):
        self._simple_click(self.LOGIN_PAGE)

    def privacy_policy(self):
        return self._element(self.PRIVACY_POLICY)

    def minor_data(self):
        self._send_keys(self.FIRST_NAME, "august")
        self._send_keys(self.LAST_NAME, "weller")
        self._send_keys(self.PHONE, "+79998887766")
        self._simple_click(self.AGREE)

    @staticmethod
    def create_email_and_pass():
        email, password = f"{random_email()}", f"{random_string()}"
        with open("data.txt", "w") as file:
            file.write("".join([email, "\n", password]))
        return email, password

    def register_account(self):
        email, password = self.create_email_and_pass()
        self._send_keys(self.EMAIL, email)
        self._send_keys(self.PASS, password)
        self._send_keys(self.CONFIRM_PASS, password)
        self.minor_data()
        self._simple_click(self.CONTINUE)

    def register_same_account(self):
        with open("data.txt", "r") as file:
            main_data = file.read()
        email, password = main_data.split("\n")
        self._send_keys(self.EMAIL, email)
        self._send_keys(self.PASS, password)
        self._send_keys(self.CONFIRM_PASS, password)
        self.minor_data()
        self._simple_click(self.CONTINUE)

    def account_created_alert(self):
        return self._element(self.SUCCESSFUL_ALERT)

    def alert_after_registration_same_user(self):
        return self._element(self.ALERT)
