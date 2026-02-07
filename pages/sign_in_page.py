from pages.base_page import Page
from selenium.webdriver.common.by import By


class SignInPage(Page):
    SIGN_IN_MSG = (By.XPATH, "//*[text()='Sign in or create account']")
    PP_LINK = (By.CSS_SELECTOR, "a[aria-label*='privacy policy']")
    TC_LINK = (By.CSS_SELECTOR, "a[aria-label*='terms']")
    expected_sign_in_msg = 'Sign in'

    def verify_sign_in_msg(self):
        self.verify_partial_text(self.expected_sign_in_msg, *self.SIGN_IN_MSG)

    def click_target_pp_link(self):
        self.wait_until_clickable_click(*self.PP_LINK)

    def click_target_tc_link(self):
        self.wait_until_clickable_click(*self.TC_LINK)