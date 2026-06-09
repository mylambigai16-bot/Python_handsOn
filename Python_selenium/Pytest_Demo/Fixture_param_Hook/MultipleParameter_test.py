import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

@pytest.mark.parametrize("browser",["Chrome","Edge"])
@pytest.mark.parametrize("app",["http://www.flipkart.com/","http://www.amazon.com/"])
def test_browser_app(browser, app):
    print("Test starts!")
    if(browser == "Chrome"):
        options = ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    elif(browser == "Edge"):
        options = EdgeOptions()
        options.add_argument("--headless")
        driver = webdriver.Edge(options=options)

    driver.maximize_window()
    driver.get(app) 
    print(app.title)
    print("Test finished!")
    driver.close()