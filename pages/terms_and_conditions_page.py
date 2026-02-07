from pages.base_page import Page


class TermsAndConditionsPage(Page):

    def verify_tc_page_opened(self):
        self.verify_partial_url('terms-conditions')