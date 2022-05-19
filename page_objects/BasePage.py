from selenium.webdriver.common.by import By
from page_objects.Actions import Actions


class BasePage(Actions):
    LOGO = (By.CSS_SELECTOR, "#logo")
    SHOPPING_CART = (By.XPATH, "//div[@id='cart']/button")
    EMPTY_CART = (By.XPATH, "//p[text()='Your shopping cart is empty!']")
    SEARCH_FIELD = (By.XPATH, "//div[@id='search']/input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".fa-search")
    NO_SEARCH_MATCHES = (By.XPATH, "//p[text()='There is no product that matches the search criteria.']")
    CURRENCY_BUTTON = (By.XPATH, "//div[@class='btn-group']/button")
    ABOUT_US = (By.LINK_TEXT, "About Us")
    COLUMN = (By.CSS_SELECTOR, ".col-sm-3")

    def click_currency_button(self):
        self._click(self.CURRENCY_BUTTON)
        return self

    def check_currencies(self):
        for i in range(1, 4):
            curr = (By.XPATH, f"//ul[@class='dropdown-menu']/li[{i}]")
            self._click(curr)
            self._click(self.CURRENCY_BUTTON)

    def logo(self):
        return self._element(self.LOGO)

    def click_logo(self):
        self._click(self.LOGO)

    def click_shopping_cart(self):
        self._click(self.SHOPPING_CART)

    def check_empty_cart(self):
        return self._element(self.EMPTY_CART)

    def search_product(self, product):
        self._send_keys(self.SEARCH_FIELD, product)
        self._click(self.SEARCH_BUTTON)

    def find_product(self, product):
        link_text = (By.LINK_TEXT, product)
        return self._element(link_text)

    def no_search_matches(self):
        return self._element(self.NO_SEARCH_MATCHES)

    def click_all_menu(self):
        self._element((By.LINK_TEXT, "Desktops"))
        self._click_link("Laptops & Notebooks")
        self._click_link("Components")
        self._click_link("Tablets")
        self._click_link("Software")
        self._click_link("Phones & PDAs")
        self._click_link("Cameras")
        self._click_link("MP3 Players")

    def click_right_menu(self):
        for i in range(1, 6):
            self._click((By.XPATH, f"//ul[@class='list-inline']/li[{i}]"))
