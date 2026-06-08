import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)
assert driver.title == "Automation Exercise"
print("Home page was launched")

driver.find_element(By.XPATH,value="//a[text()=' Signup / Login']").click()
login_page = driver.find_element(By.XPATH,value="//div[@class='login-form']/child::h2").text
assert login_page.__eq__("Login to your account")
print("Login section was displayed")

driver.find_element(By.XPATH,value="//form[@action='/login']/child::input[2]").send_keys("2k22ece056@kiot.ac.in")
driver.find_element(By.XPATH,value="//form[@action='/login']/child::input[3]").send_keys("123456")
driver.find_element(By.XPATH,value="//form[@action='/login']/child::button").click()
time.sleep(5)
logged_in = wait.until(ec.visibility_of_element_located((By.XPATH,"//ul[@class='nav navbar-nav']/child::*[10]"))).is_displayed()
assert logged_in is True
print("Logged in successfully")

action = ActionChains(driver)
action.send_keys(Keys.ARROW_LEFT).perform()
action.send_keys(Keys.ENTER).perform()
driver.find_element(By.XPATH,value="//a[text()=' Logout']").click()
time.sleep(5)
url = driver.current_url
print(url)
assert url.__eq__("https://automationexercise.com/login")
print("Logout successfull")

driver.close()