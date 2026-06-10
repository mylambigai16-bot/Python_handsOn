import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from Utilities import excelReader
from Utilities.logCreater import log_creator

logger = log_creator()

@pytest.mark.parametrize("email,password", excelReader.get_data("ExcelFile/LoginData.xlsx", "login"))
@pytest.mark.usefixtures("test_setup_and_tearDown")
@pytest.mark.order(1)  
class TestLogin:
    def test_validLogin(self, email, password):
        logger.info(f"Running test_validLogin with email: {email} password: {password}")
        self.driver.find_element(By.CSS_SELECTOR, "a[title='My Account']").click()
        self.driver.find_element(By.XPATH, "//li/a[text()='Login']").click()
        logger.info("Login...")

        self.driver.find_element(By.CSS_SELECTOR, "input[id='input-email']").send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, "input[id='input-password']").send_keys(password) 
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Login']").click()
        logger.info("Login button clicked")

        action = ActionChains(self.driver)
        action.send_keys(Keys.TAB).perform()
        action.send_keys(Keys.ENTER).perform()

        expected_url = "https://tutorialsninja.com/demo/index.php?route=account/account"
        current_url = self.driver.current_url
        print(current_url)
        assert expected_url == current_url
        logger.info("Login assertion by url")
        logger.info("Login successfull!")
