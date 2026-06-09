import pytest
from selenium import webdriver
from Utility import excelReader
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import Utility.logCreator

@pytest.mark.parametrize("Username,Password",excelReader.get_data(r"ExcelFile\LoginData.xlsx","login"))
class TestLogin:
    def test_validLogin(self,Username, Password):
        log = Utility.logCreator.log_creator()
        self.driver = webdriver.Chrome()
        log.info("Chrome browser launchhed")
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")
        log.info("Demo blaze website opened")
        self.driver.find_element(By.ID,"login2").click()
        print(Username, Password)
        wait = WebDriverWait(self.driver,15)
        wait.until(ec.visibility_of_element_located((By.ID, "loginusername"))).send_keys(Username)
        self.driver.find_element(By.ID,"loginpassword").send_keys(Password)
        log.info("Username and password get entered")
        self.driver.find_element(By.XPATH,"//button[text()='Log in']").click()
        
        log.info("Waiting for logout should display")
        wait.until(ec.visibility_of_element_located((By.ID, "logout2")))
        log.info("Logout button is displayed")
        logout = self.driver.find_element(By.ID,"logout2")
        assert logout.text == "Log out"
        log.info("Login successfull...")

        self.driver.close()
        log.info("Browser closed!")

