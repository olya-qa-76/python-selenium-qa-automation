# Import the base Page class that provides common browser actions
# such as opening URLs, clicking elements, and waiting for conditions
from pages.base_page import Page


# Define the MainPage class, which represents Target's main (home) page
# This class follows the Page Object Model and inherits shared behavior
# from the base Page class
class MainPage(Page):


    def open_main_page(self):
        self.open_url('https://www.target.com/')
        # self                      → Refers to the current Page Object instance (MainPage)
        # open_url()                → Reusable helper method (usually from a BasePage)
        # 'https://www.target.com/' → Target homepage URL the test needs to open