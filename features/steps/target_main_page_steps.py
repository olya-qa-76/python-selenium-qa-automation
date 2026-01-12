from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')  # links this function to the Gherkin step.
def open_main(context):
    context.driver.get("https://www.target.com/")  # context.driver is the Selenium WebDriver (usually created/defined in environment.py).
                                                   # .get() navigates to the Target homepage.