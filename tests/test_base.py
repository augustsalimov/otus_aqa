from page_objects.BasePage import BasePage


def test_currencies(browser):
    BasePage(browser).click_currency_button()
    BasePage(browser).check_currencies()


def test_header_2(browser):
    BasePage(browser).click_logo()
    assert BasePage(browser).logo()
    BasePage(browser).click_shopping_cart()
    assert BasePage(browser).check_empty_cart()


def test_search(browser):
    BasePage(browser).search_product("macbook")
    assert BasePage(browser).find_product("MacBook")
    assert BasePage(browser).find_product("MacBook Air")
    assert BasePage(browser).find_product("MacBook Pro")
    BasePage(browser).search_product("random")
    assert BasePage(browser).no_search_matches()


def test_navbar(browser):
    BasePage(browser).click_all_menu()


def test_right_menu(browser):
    BasePage(browser).click_right_menu()
