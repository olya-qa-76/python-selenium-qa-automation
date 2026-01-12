from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


HELP_HEADER = (By.XPATH, "//h1[text()='Help']")
TWO_ELEMENTS_BLOCK = (By.XPATH, "//div[contains(@class, 'HelpSearch')]//span[contains(@class, 'styles_textSpan')]")
BROWSE_ALL_HELP_BUTTON = (By.XPATH, "//button[text()='Browse all help']")
HELP_SEARCH_FIELD = (By.CSS_SELECTOR, "[class*='HelpSearch_typeAheadDesktop']")
HELP_SEARCH_BUTTON = (By.XPATH, "//button[text()='Search']")
WHAT_WOULD_YOU_HEADER = (By.XPATH, "//h2[text()='What would you like help with?']")
NAV_CARD_WRAPPER = (By.CSS_SELECTOR, "div[class*='NavCard_navCardWrapper']")
POP_PAGES_HEADER = (By.XPATH, "//h2[text()='Popular Pages']")
LINK_CARD_CONTAINER = (By.CSS_SELECTOR, "div[class*='LinkCard_styledCard']")


@given('Open Target Help page')
def open_target_help_page(context):
    context.driver.get('https://help.target.com/help')


@then("Verify 'Help' header")
def verify_header_exists(context):
    context.driver.find_element(*HELP_HEADER)


@then('Verify 2 elements block')
def verify_two_elements_block(context):
    context.driver.find_element(*TWO_ELEMENTS_BLOCK)


@then("Verify 'Browse all help' button")
def verify_browse_all_help_button(context):
    context.driver.find_element(*BROWSE_ALL_HELP_BUTTON)


@then("Verify 'Help Search' field")
def verify_help_search(context):
    context.driver.find_element(*HELP_SEARCH_FIELD)


@then("Verify 'Search' button")
def verify_search_button(context):
    context.driver.find_element(*HELP_SEARCH_BUTTON)


@then("Verify 'What would you like help with' header")
def verify_header(context):
    context.driver.find_element(*WHAT_WOULD_YOU_HEADER)


@then("Verify 'Navigation Card' wrapper")
def verify_nav_card_wrapper(context):
    context.driver.find_element(*NAV_CARD_WRAPPER)


@then("Verify 'Popular Pages' header")
def verify_container(context):
    context.driver.find_element(*POP_PAGES_HEADER)


@then("Verify 'Link Card' container")
def verify_link_container(context):
    context.driver.find_element(*LINK_CARD_CONTAINER)