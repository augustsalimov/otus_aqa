from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_navbar(browser):
    browser.get("https://demo.opencart.com/")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Desktops")), message="No element").click()
    browser.find_element(By.LINK_TEXT, "Laptops & Notebooks").click()
    browser.find_element(By.LINK_TEXT, "Components").click()
    browser.find_element(By.LINK_TEXT, "Tablets").click()
    browser.find_element(By.LINK_TEXT, "Software").click()
    browser.find_element(By.LINK_TEXT, "Phones & PDAs").click()
    browser.find_element(By.LINK_TEXT, "Cameras").click()
    browser.find_element(By.LINK_TEXT, "MP3 Players").click()


def test_desktops(browser):
    browser.get("https://demo.opencart.com/")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Desktops")), message="No element").click()
    browser.find_element(By.LINK_TEXT, "PC (0)")
    browser.find_element(By.LINK_TEXT, "Mac (1)").click()


def test_header(browser):
    browser.get("https://demo.opencart.com/")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Desktops")), message="No element").click()
    browser.find_element(By.LINK_TEXT, "Mac (1)").click()
    browser.find_element(By.CSS_SELECTOR, ".fa-home").click()


def test_grid(browser):
    browser.get("https://demo.opencart.com/")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tablets")), message="No element").click()
    browser.find_element(By.CSS_SELECTOR, ".fa-th-list").click()
    browser.find_element(By.CSS_SELECTOR, ".fa-th").click()


def test_camera(browser):
    browser.get("https://demo.opencart.com/")
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Cameras")), message="No element").click()
    browser.find_element(By.LINK_TEXT, "Software (0)").click()
