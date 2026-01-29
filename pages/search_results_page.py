from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SearchResultsPage(Page):
    SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-test='lp-resultsCount'] div.h-display-flex")

    def verify_search_results(self, expected_results):
        actual_results = self.find_element(*self.SEARCH_RESULTS).text
        assert expected_results in actual_results, f"Expected {expected_results}, but got {actual_results}"  # pass the `expected_product` variable from the feature file to verify results dynamically