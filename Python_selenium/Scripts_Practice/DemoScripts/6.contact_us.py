import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")
driver.maximize_window()
try:
    assert driver.title == "Automation Exercis"
except AssertionError:
    driver.save_screenshot("screenshots/login_page.png")
    raise
print("Home page was launched")

driver.find_element(By.XPATH, "//a[contains(@href,'/contact')]").click()
get_in_touch_text = driver.find_element(By.XPATH, "//div[@class='contact-form']/child::h2")
assert get_in_touch_text.is_displayed()
print("Verified Get in touch text!")

driver.find_element(By.CSS_SELECTOR, "input[placeholder='Name']").send_keys("Mugan")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email']").send_keys("mugan@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Subject']").send_keys("Nothing")
