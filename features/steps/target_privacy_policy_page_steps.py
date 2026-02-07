from behave import given, when, then
from time import sleep


@then('Verify Privacy Policy page opened')
def verify_pp_page_opened(context):
    sleep(5)  # Firefox
    context.app.privacy_policy_page.verify_pp_page_opened()


@then('User can close new window and switch back to original')
def close_and_switch_to_original_page(context):
    context.app.base_page.close_page()
    context.app.base_page.switch_to_window_by_id(context.original_window)