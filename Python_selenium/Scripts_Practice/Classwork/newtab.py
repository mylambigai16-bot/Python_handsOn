import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as ec
from datetime import datetime

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/browser-windows")

driver.find_element(By.XPATH, "//button[@class='btn btn-primary'][@id='tabButton']").click()
tab = driver.window_handles
print(tab)

driver.switch_to.window(tab[1])
driver.save_screenshot(f"screenshots/Homepage_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
con = driver.find_element(By.XPATH, "//h1").text
print(con)

driver.switch_to.window(tab[0])

driver.close()