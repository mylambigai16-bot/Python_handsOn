from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://automationexercise.com")

home = driver.find_element(By.XPATH, value="//li/a[text()=' Home']")
assert home.is_displayed()

driver.find_element(By.XPATH, "//a[@href='/products']").click()
wait = WebDriverWait(driver, 10)
action = ActionChains(driver)

add_to_cart1 = wait.until(ec.visibility_of_element_located((By.XPATH, "(//div[@class='col-sm-4']//a[@data-product-id='1'])[1]")))
action.move_to_element(add_to_cart1).perform()
add_to_cart1.click()
cont_shoppping = wait.until(ec.visibility_of_element_located((By.XPATH, "//button[text()='Continue Shopping']")))
cont_shoppping.click()

wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='modal-footer']//child::button"))).click()
add_to_cart2 = wait.until(ec.visibility_of_element_located((By.XPATH, "(//div[@class='col-sm-4']//a[@data-product-id='1'])[1]")))
action.move_to_element(add_to_cart2).perform()
add_to_cart2.click
view_cart = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='modal-body']//a[@href='/view_cart']")))
view_cart.click()


driver.close()
