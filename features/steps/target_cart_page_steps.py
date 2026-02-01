from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, "[id*='item-title']")


@when('Open Target Cart page')
def open_cart_page(context):
    context.app.cart_page.open_cart_page()


@then('Verify “Your cart is empty” message is shown')
def verify_cart_empty(context):
    context.app.cart_page.verify_empty_cart_msg()


@then('Verify Cart has more than {expected_amount} item(s)')
def verify_individual_items(context, expected_amount):
    context.app.cart_page.verify_individual_items(expected_amount)


@then('Verify product is correct in Cart')
def verify_product_name_in_cart(context):
    product_name_in_cart = context.driver.wait.until(
        EC.visibility_of_element_located(PRODUCT_NAME_IN_CART),
        message='Product name is invalid'
    ).text
    assert product_name_in_cart[:15] == context.product[:15], f"Expected: '{context.product}', but got '{product_name_in_cart}'"