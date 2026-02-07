from selenium.webdriver.common.by import By
from pages.base_page import Page


class TargetAppPage(Page):
    PP_LINK = (By.CSS_SELECTOR, "a[aria-label*='privacy policy']")
    PAGE_TITLE = (By.CSS_SELECTOR, "[data-test='page-title']")

    def open_target_app_page(self):
        self.open_url('/c/target-app')

    def click_pp_link(self):
        self.wait_until_clickable_click(*self.PP_LINK)
        print('All windows after clicking PP_Link:', self.driver.window_handles)