from behave import given, when, then


@given('Open Target main page')
def open_main(context):
    context.app.main_page.open_main_page()
    # context           → Behave's shared object that holds test state across steps
    # app               → Application container that groups all page objects
    # main_page         → Page Object representing Target's main (home) page
    # open_main_page()  → Page method that navigates the browser to the Target homepage