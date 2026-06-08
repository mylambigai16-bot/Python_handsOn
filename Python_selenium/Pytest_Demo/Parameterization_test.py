import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("search", ["Selenium", "Locator"])
def test_search(search):

    driver = webdriver.Chrome()

    driver.get("https://www.google.com")
    driver.maximize_window()

    search_bar = driver.find_element(By.NAME, "q")
    search_bar.send_keys(search)

    driver.quit()