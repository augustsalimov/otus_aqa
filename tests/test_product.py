from page_objects.ProductPage import ProductPage
from page_objects.MainPage import MainPage
from page_objects.BasePage import BasePage
import allure
import time


@allure.title("Return home from product page")
def test_home_button(browser):
    ProductPage(browser).go_to_product("MacBook")
    MainPage(browser).click_home_button()


@allure.title("Add to cart product")
def test_add_to_cart(browser):
    ProductPage(browser).go_to_product("iPhone")
    ProductPage(browser).add_to_cart()
    time.sleep(2)
    BasePage(browser).click_shopping_cart()
    assert ProductPage(browser).check_product_in_cart() == 'iPhone'


@allure.title("Click main photo")
def test_main_photo(browser):
    ProductPage(browser).go_to_product('Apple Cinema 30"')\
        .click_main_photo_and_esc()\
        .find_main_photo()


@allure.title("Click additional photos")
def test_photos(browser):
    page = ProductPage(browser)
    page.go_to_product("Samsung Galaxy Tab 10.1")\
        .find_first_little_photo()
    for i in range(1, 4):
        page.click_next()
    page.click_prev()


@allure.title("Add product to wish list and to compare")
def test_wish_list(browser):
    ProductPage(browser).go_to_product("Canon EOS 5D")\
        .add_to_wish_list()\
        .compare_product()
