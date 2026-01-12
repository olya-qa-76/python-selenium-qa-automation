from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-test='lp-resultsCount'] div.h-display-flex")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_ADD_TO_CART_BTN = (By.XPATH, "//div[@data-test='orderPickupSection']//button[text()='Add to cart']")


@then('Search results for {expected_product} are shown')
def verify_search_results(context, expected_product):
    actual = context.driver.find_element(*SEARCH_RESULTS).text
    assert expected_product in actual, f"Expected: '{expected_product}' NOT in Actual: '{actual}'"
    sleep(3)


@when('Click "Add to cart" button')
def click_add_to_cart_btn(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(2)  # Waits for Side Nav to appear

@when('Click Side Nav "Add to cart" button')
def click_side_nav_btn(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()