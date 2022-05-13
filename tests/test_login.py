from selenium.webdriver.common.by import By
from page_objects.LoginPage import LoginPage
from page_objects.RegisterPage import RegisterPage


def test_right_menu_in_login(browser):
    LoginPage(browser).click_login()
    RegisterPage(browser).click_all_elements_of_right_menu()


def test_continue_to_register(browser):
    LoginPage(browser).click_login()
    LoginPage(browser).continue_to_register()


def test_login(browser):
    LoginPage(browser).click_login()
    LoginPage(browser).login()


def test_login_inner(browser):
    LoginPage(browser).click_login()
    LoginPage(browser).login()
    LoginPage(browser).inners()


def test_change_pass(browser):
    LoginPage(browser).click_login()
    LoginPage(browser).login()
    LoginPage(browser).change_password()
