from page_objects.BasePage import BasePage
import allure


@allure.title("Click all currencies")
def test_currencies(browser):
    BasePage(browser).click_currency_button().check_currencies()


@allure.title("Testing of existence of logo and cart")
def test_header_2(browser):
    BasePage(browser).click_logo()
    assert BasePage(browser).logo()
    BasePage(browser).click_shopping_cart()
    assert BasePage(browser).check_empty_cart()


@allure.title("Testing of search field")
def test_search(browser):
    page = BasePage(browser)
    page.search_product("macbook")
    assert page.find_product("MacBook")
    assert page.find_product("MacBook Air")
    assert page.find_product("MacBook Pro")
    page.search_product("random")
    assert page.no_search_matches()


@allure.title("Clicking of menu")
def test_navbar(browser):
    BasePage(browser).click_all_menu()


@allure.title("Clicking right menu")
def test_right_menu(browser):
    BasePage(browser).click_right_menu()
