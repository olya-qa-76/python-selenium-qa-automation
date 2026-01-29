from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep
from features.steps.target_search_results_page_steps import PRODUCT_NAME

CART_TEXT = (By.XPATH, "//*[text()='Your cart is empty']")
CART_ITEMS = (By.CSS_SELECTOR, "[data-test='cartItem']")
PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, "[id*='item-title']")


@when('Open Target Cart page')
def open_cart_page(context):
    context.driver.get('https://www.target.com/cart')


@then('Verify “Your cart is empty” message is shown')
def verify_cart_empty(context):
    context.app.cart_page.verify_empty_cart()


@then('Verify Cart has more than {expected_amount} item(s)')
def verify_individual_items(context, expected_amount):
    expected_amount = int(expected_amount)
    items = context.driver.wait.until(
        EC.visibility_of_all_elements_located(CART_ITEMS),
        message='Item(s) were not found'
    )
    assert len(items) >= expected_amount, f"Expected more than or equal {expected_amount} item(s), but got {len(items)}"


@then('Verify product is correct in Cart')
def verify_product_name(context):
    product_in_cart = context.driver.wait.until(
        EC.visibility_of_element_located(PRODUCT_NAME_IN_CART),
        message='Product name is invalid'
    ).text
    assert product_in_cart[:15] == context.product[:15], f"Expected: '{context.product}', but got '{product_in_cart}'"