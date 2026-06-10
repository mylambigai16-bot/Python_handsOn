import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities.logCreator import log_creator

logger = log_creator()

class Searchpage:
    
    search_result = "HP LP3065"
    invalid_pro_msg = "//input[@id='button-search']/following-sibling::p"

    def __init__(self, driver):
        self.driver = driver

    def valid_search(self):
        assert self.driver.find_element(By.LINK_TEXT, self.search_result).is_displayed()
        logger.info("Assert by product is displayed for valid!")

    def invalid_search(self):
         expected_res = "There is no product that matches the search criteria."
         actual = self.driver.find_element(By.XPATH, self.invalid_pro_msg ).text
         print(actual)
         assert expected_res.__eq__(actual)
         logger.info("Assert the invalud search message!")
    
    