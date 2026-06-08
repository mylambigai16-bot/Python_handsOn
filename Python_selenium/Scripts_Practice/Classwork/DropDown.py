from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.leafground.com/select.xhtml")
driver.maximize_window()

#Select drop down using select class
tool = driver.find_element(By.XPATH, "//select[@class='ui-selectonemenu']")
select = Select(tool)
select.select_by_index(1)
time.sleep(2)
print("Tool selected successfully using select tag!")

# Select drop down using Action chains
country = driver.find_element(By.XPATH, "//label[@id='j_idt87:country_label']//following-sibling::div")
country.click()
action = ActionChains(driver)
time.sleep(2)
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ENTER).perform()
time.sleep(2)
print("Country selected using ActinChains!")

#click drop down and click
driver.find_element(By.XPATH, "//label[text()='Select City']").click()
wait = WebDriverWait(driver, 10)
wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='j_idt87:city_panel']//ul//li[@data-label='Bengaluru']"))).click()
print("City selected using creating custom locators and click!")

# Multiple select suggestion dropdown using iteration
course = driver.find_element(By.XPATH, "//h5[text()='Choose the Course']/following::div[@role='application']//input")
course.click()
course.send_keys("PostMan")
course_dropdown = wait.until(ec.visibility_of_all_elements_located((By.XPATH, "//span[@id='j_idt87:auto-complete_panel']/ul/li")))

for option in course_dropdown:
    print(option.text)

    if option.text.strip() == "PostMan":
        option.click()
        time.sleep(2)
        break


#Choose language 
driver.find_element(By.XPATH, "//label[@id='j_idt87:lang_label']").click()
wait.until(ec.visibility_of_element_located(By.XPATH, "//ul[@id='j_idt87:lang_items']"))
print("Select suggestion element using iterate the li tag! ")
driver.close()