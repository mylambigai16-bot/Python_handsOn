from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.com")
print(driver.title)

ele = driver.find_element(By.NAME, "q")

if ele.is_enabled():
    ele.send_keys("Selenium")
    ele.send_keys(Keys.ENTER)

time.sleep(5)
driver.quit()
