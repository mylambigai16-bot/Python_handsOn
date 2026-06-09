import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def setup_function(function):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")

def teardown_function(function):
    driver.close()

def test_valid(test_setup_and_tearDown):
    driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("HP")
    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
    assert driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()

