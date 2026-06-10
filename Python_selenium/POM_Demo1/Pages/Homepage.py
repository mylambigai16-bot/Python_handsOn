from selenium.webdriver.common.by import By
from Utilities.logCreator import log_creator

logger = log_creator()

class Homepage:

    search_bar = "//input[@placeholder='Search']"
    click_search = "//button[contains(@class,'btn-default')]"
    

    def __init__(self, driver):
        self.driver = driver

    def click_searchh(self):
        
        self.driver.find_element(By.XPATH, self.search_bar).click()
        logger.info("Search bar clicked")
        self.driver.find_element(By.XPATH, self.search_bar).send_keys("HP")
        logger.info("Enter  input to search bar")
        self.driver.find_element(By.XPATH, self.click_search).click()
        logger.info("Start searching...")

    def invalid_search(self):
         
         self.driver.find_element(By.XPATH, self.search_bar).send_keys("Honda")
         self.driver.find_element(By.XPATH, self.click_search).click()

    def no_product_search(self):

         self.driver.find_element(By.XPATH, self.search_bar).send_keys("")
         self.driver.find_element(By.XPATH, self.click_search).click()
         