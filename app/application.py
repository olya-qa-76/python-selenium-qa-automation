# Import individual Page Object classes.
# Each class represents a specific area or page of the application UI.
from pages.cart_page import Cart_Page
from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage


class Application:
# Application-level container for all Page Objects.
# This class acts as a single access point to the application under test.
# It groups all page objects together so test steps can interact with
# different parts of the UI through one shared object.

    def __init__(self, driver):
        # Initialize each Page Object with the same WebDriver instance.
        # This ensures all pages interact with the same browser session.

        self.cart_page = Cart_Page(driver)
        self.main_page = MainPage(driver)  # Represents the Target main (home) page and its actions
        self.header = Header(driver)  # Represents the common header section (search bar, navigation, etc.)
        self.search_results_page = SearchResultsPage(driver)  # Represents the search results page and product listing interactions