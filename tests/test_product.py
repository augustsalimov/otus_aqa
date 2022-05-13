from page_objects.ProductPage import ProductPage
from page_objects.MainPage import MainPage
from page_objects.BasePage import BasePage
import time


def test_home_button(browser):
    ProductPage(browser).go_to_product("MacBook")
    MainPage(browser).click_home_button()


def test_add_to_cart(browser):
    ProductPage(browser).go_to_product("iPhone")
    ProductPage(browser).add_to_cart()
    time.sleep(2)
    BasePage(browser).click_shopping_cart()
    assert ProductPage(browser).check_product_in_cart() == 'iPhone'


def test_main_photo(browser):
    ProductPage(browser).go_to_product('Apple Cinema 30"')
    ProductPage(browser).click_main_photo_and_esc()
    ProductPage(browser).find_main_photo()


def test_photos(browser):
    ProductPage(browser).go_to_product("Samsung Galaxy Tab 10.1")
    ProductPage(browser).find_first_little_photo()
    for i in range(1, 4):
        ProductPage(browser).click_next()
    ProductPage(browser).click_prev()


def test_wish_list(browser):
    ProductPage(browser).go_to_product("Canon EOS 5D")
    ProductPage(browser).add_to_wish_list()
    ProductPage(browser).compare_product()
