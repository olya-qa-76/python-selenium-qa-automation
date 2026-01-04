from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_main(context):
    context.driver.get("https://www.target.com/")


@when('Search for tea')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    context.driver.find_element(By.CSS_SELECTOR, "button[data-test='@web/Search/SearchButton']").click()
    sleep(3)  # wait for 3 seconds before search results are shown.


@then('Search results for tea are shown')
def verify_search_results(context):
    expected = 'tea'
    actual = context.driver.find_element(By.XPATH, "[data-test='lp-resultsCount']").text
    assert expected in actual, f"Expected: '{expected}' NOT in Actual: '{actual}'"


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()


@then('Verify “Your cart is empty” message is shown')
def verify_cart_empty(context):
    expected = "Your cart is empty"
    actual = context.driver.find_element(By.XPATH, "//*[text()='Your cart is empty']").text
    assert expected == actual, f"Expected: '{expected}' NOT shown, it shows actual: '{actual}'"