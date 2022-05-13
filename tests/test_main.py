from page_objects.MainPage import MainPage


def test_swipe(browser):
    MainPage(browser).swipe()


def test_main_photo(browser):
    assert MainPage(browser).main_photo_exist()


def test_main_products(browser):
    MainPage(browser).click_and_check_main_product("MacBook")
    MainPage(browser).click_and_check_main_product("iPhone")
    MainPage(browser).click_and_check_main_product('Apple Cinema 30"')
    MainPage(browser).click_and_check_main_product("Canon EOS 5D")


def test_add_product_to_cart(browser):
    product = 'MacBook'
    MainPage(browser).add_product_to_cart(f"{product}")
    MainPage(browser).check_alert(f"{product}")


def test_compare_product(browser):
    product = 'iPhone'
    MainPage(browser).add_to_compare(product)
    MainPage(browser).check_compare_alert(product)
