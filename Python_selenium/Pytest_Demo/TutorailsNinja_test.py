import pytest
import conftest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("test_setup_and_tearDown")
class searchTest:
    def test_valid(self):
         self.driver.find_element(By.NAME, "search").send_keys("HP")
         self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default)]").click()
         assert self.driver.find_element(By.LINK_TEXT, "HP LP3065")

    def test_invalid(self):
        self.driver.find_element(By.NAME, "search").send_keys("Honda")
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default)]").click()
        expected_res = "There is no product that matchs the search criteria"
        actual = self.driver.find_element(By.XPATH, "//input[@id='button-search]//following-sibling::p")
        assert expected_res.__eq__(actual)
