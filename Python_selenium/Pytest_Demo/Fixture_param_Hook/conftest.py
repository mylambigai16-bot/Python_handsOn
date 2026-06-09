import pytest
from selenium import webdriver

@pytest.fixture()
def test_setup_and_tearDown(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    request.cls.driver =driver
    yield
    driver.close()
'''
@pytest.fixture(params=['Chrome',"Firefox","Edge"])
def test_setup_and_tearDown(request):
    if request.param == "Chrome":
        driver = webdriver.Chrome()
    elif request.param =="Firefox":
        driver = webdriver.Firefox()
    elif request.param == "Edge":
        driver = webdriver.Edge()
    
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    request.cls.driver =driver
    yield
    driver.close() 
    '''