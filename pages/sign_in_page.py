from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class SignInPage(Page):
    SIGN_IN_MSG = (By.XPATH, "//*[text()='Sign in or create account']")
    expected_sign_in_msg = 'Sign in'

    def verify_sign_in_msg(self):
        self.verify_partial_text(self.expected_sign_in_msg, *self.SIGN_IN_MSG)