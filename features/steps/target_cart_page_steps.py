from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_TEXT = (By.XPATH, "//*[text()='Your cart is empty']")
CART_ITEMS = (By.CSS_SELECTOR, "[data-test='cartItem']")


@when('Open Target Cart page')
def open_cart_page(context):
    context.driver.get('https://www.target.com/cart')


@then('Verify “Your cart is empty” message is shown')
def verify_cart_empty(context):
    expected = "Your cart is empty"
    actual = context.driver.find_elements(*CART_TEXT).text
    assert expected == actual, f"Expected: '{expected}' NOT shown, it shows actual: '{actual}'"


@then('Verify Cart has more than {expected_amount} item(s)')
def verify_individual_items(context, expected_amount):
    expected_amount = int(expected_amount)
    items = context.driver.find_elements(*CART_ITEMS)
    assert len(items) >= expected_amount, f"Expected more than or equal {expected_amount} item(s), but got {len(items)}"