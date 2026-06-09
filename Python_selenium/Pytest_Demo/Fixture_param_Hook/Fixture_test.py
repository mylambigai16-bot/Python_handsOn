import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import read_config
import time

@pytest.fixture() 
def test_setup_and_tearDown():
    global driver
    driver =  webdriver.Chrome()
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    yield
    driver.close()

def test_valid(test_setup_and_tearDown):
    valid_search = read_config.get_config("search detail","valid")
    driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(valid_search)
    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
    assert driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()

def test_invalid(test_setup_and_tearDown):
     invalid_search = read_config.get_config("search detail","invalid")
     driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(invalid_search)
     driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
     time.sleep(5)
     expected_res = "There is no product that matches the search criteria."
     actual = driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text
     print(actual)
     time.sleep(3)
     assert expected_res.__eq__(actual)

def test_noProduct(test_setup_and_tearDown):
    driver.find_element(By.NAME, "search").send_keys("")
    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
    expected_res = "There is no product that matches the search criteria."
    actual = driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text
    time.sleep(3)
    assert expected_res.__eq__(actual)