from page_objects.MainPage import MainPage
import allure


@allure.title("Swipe main photo")
def test_swipe(browser):
    MainPage(browser).swipe().swipe()


@allure.title("Existence of main photo")
def test_main_photo(browser):
    assert MainPage(browser).main_photo_exist()


@allure.title("Click all main products")
def test_main_products(browser):
    MainPage(browser).click_and_check_main_product("MacBook")\
        .click_and_check_main_product("iPhone")\
        .click_and_check_main_product('Apple Cinema 30"')\
        .click_and_check_main_product("Canon EOS 5D")


@allure.title("Adding product to cart")
def test_add_product_to_cart(browser):
    product = 'MacBook'
    MainPage(browser).add_product_to_cart(product).check_alert(product)


@allure.title("Compare product")
def test_compare_product(browser):
    product = 'iPhone'
    MainPage(browser).add_to_compare(product).check_compare_alert(product)
