from page_objects.LoginPage import LoginPage
from page_objects.RegisterPage import RegisterPage
import allure


@allure.title("Right menu in login page")
def test_right_menu_in_login(browser):
    browser.get('/index.php?route=account/login')
    # LoginPage(browser).click_login()
    RegisterPage(browser).click_all_elements_of_right_menu()


@allure.title("Go to registration page if you don't have account")
def test_continue_to_register(browser):
    LoginPage(browser).click_login().continue_to_register()


@allure.title("Login")
def test_login(browser):
    LoginPage(browser).click_login().login()


@allure.title("Login inner page")
def test_login_inner(browser):
    LoginPage(browser).click_login().login()
    LoginPage(browser).inners()


@allure.title("Change password")
def test_change_pass(browser):
    LoginPage(browser).click_login().login()
    LoginPage(browser).change_password()
