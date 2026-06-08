from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")
driver.find_element(By.XPATH, "//button[@id='windowButton']").click()

windows = driver.window_handles
print(windows)

driver.switch_to.window(windows[1])
newWindow_text  = driver.find_element(By.ID, "sampleHeading")
print(newWindow_text.text)

driver.switch_to.window(windows[0])
driver.get_screenshot_as_file("screenshots/page.png")
driver.save_screenshot("screenshots/ss1.png")

driver.close()
