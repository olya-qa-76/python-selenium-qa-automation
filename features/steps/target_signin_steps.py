from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click "Account" button')
def click_account(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()


@when('From right side navigation menu, click "Sign In" button')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()


@then('Verify Sign In form opened')
def verify_sign_in(context):
    expected = 'Sign in'
    actual = context.driver.find_element(By.XPATH, "//*[text()='Sign in or create account']").text
    assert expected in actual, f"Expected: '{expected}' NOT in actual: '{actual}'"