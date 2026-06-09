import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import read_config

@pytest.mark.usefixtures("test_setup_and_tearDown")
class searchTest:
    def test_valid(self):
         valid_search = read_config.get_config("search detail","valid")
         self.driver.find_element(By.NAME, "search").send_keys(valid_search)
         self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
         assert self.driver.find_element(By.LINK_TEXT, "HP LP3065")

    def test_invalid(self):
        invalid_search = read_config.get_config("search detail","invalid")
        self.driver.find_element(By.NAME, "search").send_keys(invalid_search)
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
        expected_res = "There is no product that matchs the search criteria"
        actual = self.driver.find_element(By.XPATH, "//input[@id='button-search]/following-sibling::p").text
        assert expected_res.__eq__(actual)
