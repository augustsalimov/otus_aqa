from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_logo(browser):
    browser.get("https://demo.opencart.com/")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#logo")), message="No element")


def test_search(browser):
    browser.get("https://demo.opencart.com/")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.NAME, "search")), message="No element").send_keys("macbook")
    browser.find_element(By.CSS_SELECTOR, ".fa-search").click()
    browser.find_element(By.LINK_TEXT, "MacBook").click()


def test_navbar(browser):
    browser.get("https://demo.opencart.com/")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Desktops")), message="No element")
    browser.find_element(By.LINK_TEXT, "Components")
    browser.find_element(By.LINK_TEXT, "Tablets")
    browser.find_element(By.LINK_TEXT, "Software")


def test_swipe(browser):
    browser.get("https://demo.opencart.com/")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".swiper-button-next")), message="No element").click()
    browser.find_element(By.CSS_SELECTOR, ".swiper-button-next").click()
    browser.find_element(By.CSS_SELECTOR, ".swiper-button-next").click()


def test_information(browser):
    browser.get("https://demo.opencart.com/")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "About Us")), message="No element").click()
    browser.find_element(By.LINK_TEXT, "Delivery Information").click()
    browser.find_element(By.LINK_TEXT, "Privacy Policy").click()
