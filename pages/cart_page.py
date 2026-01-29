from pages.base_page import Page
from selenium.webdriver.common.by import By


class Cart_Page(Page):
    CART_TEXT = (By.XPATH, "//*[text()='Your cart is empty']")

    def verify_empty_cart(self):
        expected_text = "Your cart is empty"
        actual_text = self.find_element(*self.CART_TEXT).text
        assert expected_text in actual_text, f"Expected: '{expected_text}' is shown, but got actual: '{actual_text}'"
