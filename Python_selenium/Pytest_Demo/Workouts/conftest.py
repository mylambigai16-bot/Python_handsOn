import pytest
from selenium import webdriver
import read_config

url = read_config.get_config("Basic info", "url")
browser = read_config.get_config("Basic info", "browser")

@pytest.fixture()
def test_setup_and_tearDown(request):
    global driver
    if browser == "Chrome":
        driver = webdriver.Chrome()
    elif browser =="Firefox":
        driver = webdriver.Firefox()
    elif browser == "Edge":
        driver = webdriver.Edge()
    driver.maximize_window()
    driver.get(url)
    request.cls.driver =driver
    yield
    driver.close()