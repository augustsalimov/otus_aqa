from page_objects.RegisterPage import RegisterPage
import allure


@allure.title("Testing of right menu")
def test_right_menu(browser):
    RegisterPage(browser).click_register()
    RegisterPage(browser).click_all_elements_of_right_menu()


@allure.title("Clicking between register and login page")
def test_change_to_login_page(browser):
    RegisterPage(browser).click_register()
    RegisterPage(browser).click_login()
    RegisterPage(browser).click_register()
    RegisterPage(browser).go_to_login_page()


@allure.title("Existence of privacy policy button")
def test_privacy_policy(browser):
    RegisterPage(browser).click_register()
    assert RegisterPage(browser).privacy_policy()


@allure.title("Register user")
def test_register(browser):
    RegisterPage(browser).click_register()
    RegisterPage(browser).register_account()
    assert RegisterPage(browser).account_created_alert()


@allure.title("Register same user")
def test_register_2(browser):
    RegisterPage(browser).click_register()
    RegisterPage(browser).register_same_account()
    assert RegisterPage(browser).alert_after_registration_same_user()
