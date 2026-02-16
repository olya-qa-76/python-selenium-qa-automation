from pages.base_page import Page
from selenium.webdriver.common.by import By


class CartPage(Page):
    EMPTY_CART_TEXT = (By.XPATH, "//*[text()='Your cart is empty']")
    CART_ITEMS = (By.CSS_SELECTOR, "[data-test='cartItem']")
    empty_cart_msg = "Your cart is empty"

    def open_cart_page(self):
        self.open_url(end_url='/cart')

    def verify_empty_cart_msg(self):
        self.verify_partial_text(self.empty_cart_msg, *self.EMPTY_CART_TEXT)

        # empty_msg_element = self.find_element(*self.EMPTY_CART_TEXT)
        # print(empty_msg_element)
        # print(empty_msg_element.text)
        #
        # self.driver.refresh()  # refresh the webpage
        #
        # print('\nAfter Refresh: \n')
        #
        # empty_msg_element = self.find_element(*self.EMPTY_CART_TEXT)
        # print(empty_msg_element)
        # print(empty_msg_element.text)

    def verify_individual_items(self, expected_amount):
        expected_amount = int(expected_amount)
        items = self.find_elements(*self.CART_ITEMS)
        assert len(items) >= expected_amount, f"Expected more than or equal {expected_amount} item(s), but got {len(items)}"