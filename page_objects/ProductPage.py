import time
from selenium.webdriver.common.by import By
from page_objects.Actions import Actions


class ProductPage(Actions):
    SEARCH_FIELD = (By.XPATH, "//div[@id='search']/input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".fa-search")
    ADD_TO_CART = (By.XPATH, "//button[@id='button-cart']")
    PRODUCT_IN_CART = (By.XPATH, "//td[@class='text-left']/a")
    MAIN_PHOTO = (By.XPATH, "//ul[@class='thumbnails']/li[1]/a")
    FIRST_LITTLE_PHOTO = (By.XPATH, "//ul[@class='thumbnails']/li[2]/a")
    ESC_BUTTON = (By.XPATH, "//button[@title='Close (Esc)']")
    NEXT = (By.XPATH, "//button[@title='Next (Right arrow key)']")
    PREV = (By.XPATH, "//button[@title='Previous (Left arrow key)']")

    def go_to_product(self, product):
        self._send_keys(self.SEARCH_FIELD, product)
        self._click(self.SEARCH_BUTTON)
        time.sleep(2)
        self._simple_click((By.XPATH, f"//h4/a[text()='{product}']"))

    def go_back(self, where):
        self._click((By.XPATH, f"//a[text()='{where}']"))

    def add_to_cart(self):
        self._click(self.ADD_TO_CART)

    def check_product_in_cart(self):
        return self._element(self.PRODUCT_IN_CART).text

    def click_esc(self):
        self._click(self.ESC_BUTTON)

    def click_main_photo_and_esc(self):
        self._click(self.MAIN_PHOTO)
        self.click_esc()

    def find_main_photo(self):
        self._element(self.MAIN_PHOTO)

    def find_first_little_photo(self):
        self._click(self.FIRST_LITTLE_PHOTO)

    def click_next(self):
        self._click(self.NEXT)

    def click_prev(self):
        self._click(self.PREV)

    def add_to_wish_list(self):
        self._click((By.CSS_SELECTOR, ".fa-heart"))

    def compare_product(self):
        self._click((By.CSS_SELECTOR, ".fa-exchange"))
