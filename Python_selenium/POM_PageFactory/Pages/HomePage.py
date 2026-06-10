from seleniumpagefactory.Pagefactory import PageFactory
from Utilities.logCreator import log_creator

logger = log_creator()

class HomePage(PageFactory):

    locators = {
        'search': ('XPATH', "//input[@placeholder='Search']"),
        'search_click': ('XPATH', "//button[contains(@class,'btn-default')]")
    }

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def click_searchh(self):

        self.search.click()
        logger.info("Search bar clicked")

        self.search.set_text("HP")
        logger.info("Entered input to search bar")

        self.search_click.click()
        logger.info("Start searching...")

    def invalid_search(self):
         
         self.search.set_text("Honda")

         self.search_click.click()