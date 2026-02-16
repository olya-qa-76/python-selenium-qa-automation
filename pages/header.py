from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_ICON = (By.CSS_SELECTOR, "button[data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
    ACCOUNT_BTN = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    SIDE_NAV_ACCOUNT_BTN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")

    def search(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.wait_until_clickable_click(*self.SEARCH_ICON)
        sleep(10)

    def click_cart_icon(self):
        self.wait_until_clickable_click(*self.CART_ICON)

    def click_account_btn(self):
        self.wait_until_clickable_click(*self.ACCOUNT_BTN)

    def click_side_nav_account_btn(self):
        self.wait_until_clickable_click(*self.SIDE_NAV_ACCOUNT_BTN)