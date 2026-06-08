import pytest
from selenium import webdriver

@pytest.fixture()
def test_setup_and_tearDown(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
    request.cls.driver =driver
    yield
    driver.close()