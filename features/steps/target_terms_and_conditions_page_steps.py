from behave import given, when, then


@then('Verify Terms and Conditions page opened')
def verify_tc_page_opened(context):
    context.app.terms_and_conditions_page.verify_tc_page_opened()