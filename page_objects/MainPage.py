from selenium.webdriver.common.by import By
from page_objects.Actions import Actions


class MainPage(Actions):
    SWIPE_NEXT = (By.XPATH, "//div[contains(@class, 'slideshow0')]/span[2]")
    SWIPE_PREV = (By.XPATH, "//div[contains(@class, 'slideshow0')]/span[1]")
    MAIN_PHOTO = (By.CSS_SELECTOR, "#slideshow0")
    HOME_BUTTON = (By.CSS_SELECTOR, ".fa-home")

    def swipe(self):
        self._click(self.SWIPE_NEXT)
        self._click(self.SWIPE_PREV)
        self._click(self.SWIPE_NEXT)
        self._click(self.SWIPE_PREV)

    def main_photo_exist(self):
        return self._element(self.MAIN_PHOTO)

    def click_home_button(self):
        self._click(self.HOME_BUTTON)

    def click_and_check_main_product(self, product):
        self._simple_click_link(f"{product}")
        self._element((By.XPATH, f"//h1[text()='{product}']"))
        self.click_home_button()

    def add_product_to_cart(self, product):
        self._simple_click((By.XPATH, f"//a[text()='{product}']/../../../div[@class='button-group']/button[1]"))

    def check_alert(self, product):
        self._element((By.XPATH, f"//div[@id='common-home']/div[1]/a[text()='{product}']"))

    def add_to_compare(self, product):
        self._simple_click((By.XPATH, f"//a[text()='{product}']/../../../div[@class='button-group']/button[3]"))

    def check_compare_alert(self, product):
        self._element((By.XPATH, f"//div[@id='common-home']/div[1]/a[text()='{product}']"))
