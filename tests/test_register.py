import time
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_list_group_item(browser):
    browser.get("https://demo.opencart.com/")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".caret")), message="No element").click()
    browser.find_element(By.LINK_TEXT, "Register").click()
    browser.find_element(By.LINK_TEXT, "Login")
    browser.find_element(By.LINK_TEXT, "Register")
    browser.find_element(By.LINK_TEXT, "Forgotten Password")
    browser.find_element(By.LINK_TEXT, "My Account")


def test_navbar(browser):
    browser.get("https://demo.opencart.com/")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".caret")), message="No element").click()
    browser.find_element(By.LINK_TEXT, "Register").click()
    browser.find_element(By.LINK_TEXT, "login page")


def test_privacy_policy(browser):
    browser.get("https://demo.opencart.com/")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".caret")), message="No element").click()
    browser.find_element(By.LINK_TEXT, "Register").click()
    browser.find_element(By.LINK_TEXT, "Privacy Policy")


def test_register(browser):
    browser.get("https://demo.opencart.com/")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".caret")), message="No element").click()
    browser.find_element(By.LINK_TEXT, "Register").click()
    browser.find_element(By.CSS_SELECTOR, "#input-firstname").send_keys("august")
    browser.find_element(By.CSS_SELECTOR, "#input-lastname").send_keys("weller")
    browser.find_element(By.CSS_SELECTOR, "#input-email").send_keys(f"augustweller_{datetime.now()}@mail.com")
    browser.find_element(By.CSS_SELECTOR, "#input-telephone").send_keys("+79998765432")
    browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys("123456789")
    browser.find_element(By.CSS_SELECTOR, "#input-confirm").send_keys("123456789")
    browser.find_element(By.NAME, "agree").click()
    browser.find_element(By.XPATH, "//input[@value='Continue']").click()


def test_register_2(browser):
    browser.get("https://demo.opencart.com/")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".caret")), message="No element").click()
    browser.find_element(By.LINK_TEXT, "Register").click()
    browser.find_element(By.CSS_SELECTOR, "#input-firstname").send_keys("august")
    browser.find_element(By.CSS_SELECTOR, "#input-lastname").send_keys("weller")
    browser.find_element(By.CSS_SELECTOR, "#input-email").send_keys("augustweller@mail.com")
    browser.find_element(By.CSS_SELECTOR, "#input-telephone").send_keys("+79998765432")
    browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys("123456789")
    browser.find_element(By.CSS_SELECTOR, "#input-confirm").send_keys("123456789")
    browser.find_element(By.NAME, "agree").click()
    browser.find_element(By.XPATH, "//input[@value='Continue']").click()
    browser.find_element(By.CSS_SELECTOR, "#alert")
