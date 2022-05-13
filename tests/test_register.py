from page_objects.RegisterPage import RegisterPage


def test_right_menu(browser):
    RegisterPage(browser).click_register()
    RegisterPage(browser).click_all_elements_of_right_menu()


def test_change_to_login_page(browser):
    RegisterPage(browser).click_register()
    RegisterPage(browser).click_login()
    RegisterPage(browser).click_register()
    RegisterPage(browser).go_to_login_page()


def test_privacy_policy(browser):
    RegisterPage(browser).click_register()
    assert RegisterPage(browser).privacy_policy()


def test_register(browser):
    RegisterPage(browser).click_register()
    RegisterPage(browser).register_account()
    assert RegisterPage(browser).account_created_alert()


def test_register_2(browser):
    RegisterPage(browser).click_register()
    RegisterPage(browser).register_same_account()
    assert RegisterPage(browser).alert_after_registration_same_user()
