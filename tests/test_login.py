import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_list_group_item(browser):
    browser.get("https://demo.opencart.com/")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".caret")), message="No element").click()
    browser.find_element(By.LINK_TEXT, "Login").click()
    browser.find_element(By.LINK_TEXT, "Login")
    browser.find_element(By.LINK_TEXT, "Register")
    browser.find_element(By.LINK_TEXT, "Forgotten Password")
    browser.find_element(By.LINK_TEXT, "My Account")


def test_register(browser):
    browser.get("https://demo.opencart.com/")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".caret")), message="No element").click()
    browser.find_element(By.LINK_TEXT, "Login").click()
    browser.find_element(By.LINK_TEXT, "Continue").click()


def test_login(browser):
    browser.get("https://demo.opencart.com/")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".caret")), message="No element").click()
    browser.find_element(By.LINK_TEXT, "Login").click()
    browser.find_element(By.CSS_SELECTOR, "#input-email").send_keys("augustweller@mail.com")
    browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys("123456789")
    browser.find_element(By.XPATH, "//input[@value='Login']").click()


def test_login_inner(browser):
    browser.get("https://demo.opencart.com/")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".caret")), message="No element").click()
    browser.find_element(By.LINK_TEXT, "Login").click()
    browser.find_element(By.CSS_SELECTOR, "#input-email").send_keys("augustweller@mail.com")
    browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys("123456789")
    browser.find_element(By.XPATH, "//input[@value='Login']").click()
    browser.find_element(By.LINK_TEXT, "Edit your account information")
    browser.find_element(By.LINK_TEXT, "Change your password")


def test_change_pass(browser):
    browser.get("https://demo.opencart.com/")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".caret")), message="No element").click()
    browser.find_element(By.LINK_TEXT, "Login").click()
    browser.find_element(By.CSS_SELECTOR, "#input-email").send_keys("augustweller@mail.com")
    browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys("123456789")
    browser.find_element(By.XPATH, "//input[@value='Login']").click()
    browser.find_element(By.LINK_TEXT, "Change your password").click()
    browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys("000")
    browser.find_element(By.CSS_SELECTOR, "#input-confirm").send_keys("000")
    time.sleep(10)
