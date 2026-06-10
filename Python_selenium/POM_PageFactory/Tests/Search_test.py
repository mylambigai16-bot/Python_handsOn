import pytest
from Pages.SearchPage import Searchpage
from Pages.HomePage import HomePage
from Utilities.logCreator import log_creator

logger = log_creator()
@pytest.mark.usefixtures("test_setup_and_tearDown")
class TestSearch:

    def test_search_valid(self):

        homepage = HomePage(self.driver)
        searchpage = Searchpage(self.driver)

        logger.info("valid search")
        homepage.click_searchh()
        searchpage.valid_search()
        logger.info("valid search successful")

    def test_search_invalid(self):
         
        homepage = HomePage(self.driver)
        searchpage = Searchpage(self.driver)
        logger.info("invalid search")
        homepage.invalid_search()
        searchpage.invalid_search()
        logger.info("Invalid search successful")
