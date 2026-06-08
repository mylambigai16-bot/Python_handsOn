import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def test_setup_and_tearDown():
    global driver
    driver =  webdriver.Chrome()
    driver.get("http://tutorailsninja.com/demo/")
    driver.maximize_window()
    yield
    driver.close()

def test_valid(test_setup_and_tearDown):
    driver.find_element(By.NAME, "search").send_keys("HP")
    driver.find_element(By.XPATH, "").click()
    assert driver.find_element(By.LINK_TEXT, "HP LP3065")

def test_invalid(test_setup_and_tearDown):
     driver.find_element(By.NAME, "search").send_keys("Honda")
     driver.find_element(By.XPATH, "//button[contains(@class,'btn-default)]").click()
     expected_res = "There is no product that matchs the search criteria"
     actual = driver.find_element(By.XPATH, "//input[@id='button-search]//following-sibling::p")
     assert expected_res.__eq__(actual)

def test_noProduct(test_setup_and_tearDown):
    driver.find_element(By.NAME, "search").send_keys("")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default)]").click()
    expected_res = "There is no product that matchs the search criteria"
    actual = driver.find_element(By.XPATH, "//input[@id='button-search]//following-sibling::p")
    assert expected_res.__eq__(actual)