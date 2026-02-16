from behave import given, when, then


@given('Open sign in page')
def open_sign_in_page(context):
    context.driver.get('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_request_username&signin_amr=true')


@then('Verify Sign In form opened')
def verify_sign_in_msg(context):
    context.app.sign_in_page.verify_sign_in_msg()


@when('Click on Target privacy policy link')
def click_target_pp_link(context):
    context.app.sign_in_page.click_target_pp_link()


@when('Click on Target terms and conditions link')
def click_target_tc_link(context):
    context.app.sign_in_page.click_target_tc_link()