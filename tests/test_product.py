from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_macbook(browser):
    browser.get("https://demo.opencart.com/")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.NAME, "search")), message="No element").send_keys("macbook")
    browser.find_element(By.CSS_SELECTOR, ".fa-search").click()
    browser.find_element(By.LINK_TEXT, "MacBook").click()


def test_iphone(browser):
    browser.get("https://demo.opencart.com/")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.NAME, "search")), message="No element").send_keys("iPhone")
    browser.find_element(By.CSS_SELECTOR, ".fa-search").click()
    browser.find_element(By.LINK_TEXT, "iPhone").click()
    browser.find_element(By.CSS_SELECTOR, "#button-cart").click()


def test_photos(browser):
    browser.get("https://demo.opencart.com/")
    browser.find_element(By.LINK_TEXT, 'Apple Cinema 30"').click()
    browser.find_element(By.CSS_SELECTOR, ".thumbnail").click()
    browser.find_element(By.CSS_SELECTOR, ".mfp-img").click()


def test_wish_list(browser):
    browser.get("https://demo.opencart.com/")
    browser.find_element(By.LINK_TEXT, 'Canon EOS 5D').click()
    browser.find_element(By.CSS_SELECTOR, ".fa-heart").click()
    browser.find_element(By.CSS_SELECTOR, ".fa-shopping-cart").click()


def test_tablet(browser):
    browser.get("https://demo.opencart.com/")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.NAME, "search")), message="No element").send_keys("tab")
    browser.find_element(By.CSS_SELECTOR, ".fa-search").click()
    browser.find_element(By.LINK_TEXT, "Samsung Galaxy Tab 10.1").click()
    browser.find_element(By.CSS_SELECTOR, "#button-cart").click()
    browser.find_element(By.CSS_SELECTOR, "#cart-total").click()
    browser.find_element(By.CSS_SELECTOR, ".fa-shopping-cart").click()
