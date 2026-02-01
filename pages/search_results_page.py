from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultsPage(Page):
    SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-test='lp-resultsCount'] div.h-display-flex")
    AD_BANNER = (By.CSS_SELECTOR, "img.heroImg")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")

    def verify_search_results(self, expected_product):
        self.verify_partial_text(expected_product,*self.SEARCH_RESULTS)

    def click_add_to_cart_btn(self):
        self.wait_until_element_invisible(*self.AD_BANNER)
        self.wait_until_clickable_click(*self.ADD_TO_CART_BTN)

    def click_side_nav_add_to_cart_btn(self):
        self.wait_until_clickable_click(*self.SIDE_NAV_ADD_TO_CART_BTN)