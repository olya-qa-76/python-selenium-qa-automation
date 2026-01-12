from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# We define the locator once and use it many times in multiple steps.
SEARCH_FIELD = (By.ID, 'search')
SEARCH_ICON = (By.CSS_SELECTOR, "button[data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()


@when('Search for {product}')  # In the behave BDD framework,
# step_parameters allow you to pass dynamic values from your feature files
# to your Python step definitions, making steps reusable and readable
def search_product(context, product):  # Make sure you put the 'step_parameter' after 'context' in the function: (context, step_parameter)
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_ICON).click()
    sleep(15)  # wait for 15 seconds for 'Ad' banner to disappear


@then('Verify {expected_links} header links are shown')  # {expected_links} captures the number from the feature file.
                                                         # Behave passes it as a string by default.
def verify_header_links(context, expected_links):
    expected_amount = int(expected_links)  # Converts the string "6" → integer 6.
    links = context.driver.find_elements(*HEADER_LINKS)  # find_elements returns a list, will never throw ExceptionError incase the locator fails find the element (empty list if nothing found).
                                                         # Safe for count-based assertions.
    assert len(links) == expected_amount, f'Expected {expected_amount} header links, but got {len(links)}'  # compare actual vs expected count.