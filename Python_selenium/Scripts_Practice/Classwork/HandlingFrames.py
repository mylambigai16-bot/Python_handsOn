from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://letcode.in/frame")

frames = driver.find_element(By.XPATH, "//iframe[@src='frameui']")
driver.switch_to.frame(frames)
driver.find_element(By.XPATH, "//input[@placeholder='Enter name']").send_keys("Myl")
driver.find_element(By.XPATH, "//input[@placeholder='Enter email'][@name='lname']").send_keys("G")
inner_frame = driver.find_element(By.XPATH, "//iframe[@src='innerframe']")
driver.switch_to.frame(inner_frame)
driver.find_element(By.XPATH, "//input[@placeholder='Enter email'][@name='email']").send_keys("mugai@gmail.com")
print("Switch to frame successfully!")
driver.close()


   