from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click "Account" button')
def click_account_btn(context):
    context.app.header.click_account_btn()


@when('From right side navigation menu, click "Sign In" button')
def click_side_nav_account_btn(context):
    context.app.header.click_side_nav_account_btn()


@then('Verify Sign In form opened')
def verify_sign_in_msg(context):
    context.app.sign_in_page.verify_sign_in_msg()