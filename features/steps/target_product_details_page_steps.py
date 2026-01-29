from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "li[class*='CarouselItem'] img")
COLOR_NAMES = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")


@given('Open Target Product A-90806793 page')
def open_product_page(context):
    context.driver.get('https://www.target.com/p/men-s-relaxed-fit-jeans-goodfellow-co/-/A-90806793?preselect=90509142#lnk=sametab')


@then('Verify user can click through colors')
def verify_colors(context):
    expected_colors = ['Light Wash','Dark Wash','Indigo','Tan']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for c in colors:
        c.click()

        selected_color = context.driver.find_element(*COLOR_NAMES).text
        selected_color = selected_color.split('\n')[1]

        actual_colors.append(selected_color)
        sleep(1)

    assert set(expected_colors) == set(actual_colors), f"Expected colors: {expected_colors}, but got actual colors: {actual_colors}"