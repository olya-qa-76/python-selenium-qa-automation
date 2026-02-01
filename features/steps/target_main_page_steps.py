from behave import given, when, then


@given('Open Target main page')
def open_main_page(context):
    context.app.main_page.open_main_page()