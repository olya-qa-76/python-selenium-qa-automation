from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


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


@given('Open Help page for Returns')
def open_help_for_returns(context):
    context.app.help_page.open_help_returns()


@when('Select Help topic {option_value}')
def select_topic(context, option_value):
    context.app.help_page.select_topic(option_value)


@then("Verify 'Help' header")
def verify_header_exists(context):
    context.driver.wait.until(
        EC.visibility_of_element_located(HELP_HEADER),
        message='Help header not displayed'
    )


@then('Verify 2 elements block')
def verify_two_elements_block(context):
    context.driver.wait.until(
        EC.visibility_of_all_elements_located(TWO_ELEMENTS_BLOCK),
        message='Elements block not displayed'
    )


@then("Verify 'Browse all help' button")
def verify_browse_all_help_button(context):
    context.driver.wait.until(
        EC.visibility_of_element_located(BROWSE_ALL_HELP_BUTTON),
        message='Browse All Help button not displayed'
    )


@then("Verify 'Help Search' field")
def verify_help_search(context):
    context.driver.wait.until(
        EC.visibility_of_element_located(HELP_SEARCH_FIELD),
        message='Help Search Field not displayed'
    )


@then("Verify 'Search' button")
def verify_search_button(context):
    context.driver.wait.until(
        EC.visibility_of_element_located(HELP_SEARCH_BUTTON),
        message='Search button not displayed'
    )


@then("Verify 'What would you like help with' header")
def verify_header(context):
    context.driver.wait.until(
        EC.visibility_of_element_located(WHAT_WOULD_YOU_HEADER),
        message='What Would You Like Help with header not displayed'
    )


@then("Verify 'Navigation Card' wrapper")
def verify_nav_card_wrapper(context):
    context.driver.wait.until(
        EC.visibility_of_element_located(NAV_CARD_WRAPPER),
        message='Navigation Card wrapper not displayed'
    )


@then("Verify 'Popular Pages' header")
def verify_container(context):
    context.driver.wait.until(
        EC.visibility_of_element_located(POP_PAGES_HEADER),
        message='Popular Pages header is not displayed'
    )


@then("Verify 'Link Card' container")
def verify_link_container(context):
    context.driver.wait.until(
        EC.visibility_of_element_located(LINK_CARD_CONTAINER),
        message='Link Card container is not displayed'
    )


@then('Verify help {topic} page opened')
def verify_help_returns_opened(context, topic):
    context.app.help_page.verify_help_topic_opened(topic)


# @then('Verify help Returns page opened')
# def verify_returns_opened(context):
#     context.app.help_page.verify_returns_opened()