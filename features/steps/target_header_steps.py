from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")


@when('Click on Cart icon')
def click_cart(context):
    context.app.header.click_cart_icon()


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search(product)


@then('Verify {expected_links} header links are shown')
def verify_header_links(context, expected_links):
    expected_amount = int(expected_links)
    links = context.driver.wait.until(
        EC.visibility_of_all_elements_located(HEADER_LINKS),
        message='Header links are not visible.'
    )
    assert len(links) == expected_amount, f'Expected {expected_amount} header links, but got {len(links)}'