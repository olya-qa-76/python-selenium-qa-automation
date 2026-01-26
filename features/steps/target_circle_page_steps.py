from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


STORYCARDS = (By.CSS_SELECTOR, "[data-test='storyblock-storyblockLinkWrapper']")


@given('Open Target Circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify there are {expected_amount} storycards under “Unlock added value”')  # used {expected_amount} step parameter (type: string) for dynamic code
def verify_target_circle_storycards(context, expected_amount):  # NB: pass 'expected_amount' to the function
    expected_amount = int(expected_amount)  # convert step_parameter type: (str) "2" => 2 (int)
    # story_cards = context.driver.find_elements(*STORYCARDS)  # using find_elements: returns a list of all matching elements
    story_cards = context.driver.wait.until(
        EC.visibility_of_all_elements_located(STORYCARDS),
        message='Story cards are not visible'
    )
    assert expected_amount == len(story_cards), f"Expected {expected_amount} storycards, but got {len(story_cards)}"