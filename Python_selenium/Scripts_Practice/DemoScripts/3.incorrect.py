import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")
driver.maximize_window()
assert driver.title == "Automation Exercise"
print("In Home page!")

driver.find_element(By.XPATH,value="//a[text()=' Signup / Login']").click()
login_page = driver.find_element(By.XPATH,value="//div[@class='login-form']/child::h2").text
assert login_page.__eq__("Login to your account")
print("Login successful!")

driver.find_element(By.XPATH,value="//form[@action='/login']/child::input[2]").send_keys("muga@gmail.com")
driver.find_element(By.XPATH,value="//form[@action='/login']/child::input[3]").send_keys("123456")
driver.find_element(By.XPATH,value="//form[@action='/login']/child::button").click()
invalid_text = driver.find_element(By.XPATH, "//form[@action='/login']//child::p").text
print(invalid_text)
assert invalid_text.lower() == "your email or password is incorrect!"
print("Get invalid text!")

driver.close()
