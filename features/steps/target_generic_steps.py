from behave import given, when, then


@given('Store original window')  # we use this step just because we intent to return to it in another step
def store_original_window(context):
    context.original_window = context.app.base_page.get_current_window_handle()  # we store the variable in 'context' so we can have access to it in other steps
    print('Original window:', context.original_window)
    print('All windows:', context.driver.window_handles)  # window_handles: returns ['all current windows']


@when('Switch to new window')
def switch_to_new_window(context):
    context.app.base_page.switch_to_new_window()



@then('Close current page')
def close_current_page(context):
    context.app.base_page.close_page()  # NB: 1/ connect to the base_page() directly and call the close_page() method (no need to inherit Page class).
                                        #     2/ add base_page() reference to the application.py file


@then('Return to original window')
def return_to_original_window(context):
    context.app.base_page.switch_to_window_by_id(context.original_window)  # we pass the earlier stored 'context.original_window' as an argument in 'switch_to_window_by_id' method
    # print('Original window:', context.original_window)