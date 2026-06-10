import pytest
from Pages.SearchPage import Searchpage
from Pages.Homepage import Homepage
from Utilities.logCreator import log_creator

logger = log_creator()
@pytest.mark.usefixtures("test_setup_and_tearDown")
class TestSearch:

    def test_search_valid(self):

        homepage = Homepage(self.driver)
        searchpage = Searchpage(self.driver)

        logger.info("Home page calling...")
        logger.info("Search page calling...")
        homepage.click_searchh()
        searchpage.valid_search()
        
    def test_search_invalid(self):
         
        homepage = Homepage(self.driver)
        searchpage = Searchpage(self.driver)
        logger.info("invalid search")
        homepage.invalid_search()
        searchpage.invalid_search()
        logger.info("Invalid search successful")

    def test_no_product_search(self):

        homepage = Homepage(self.driver)
        searchpage = Searchpage(self.driver)
        logger.info("invalid search")
        homepage.no_product_search()
        searchpage.invalid_search()
        logger.info("Invalid search successful")
