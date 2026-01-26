from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "li[class*='CarouselItem'] img")  # Locator for all color swatch images displayed on the product page
COLOR_NAMES = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")  # Locator for the section that displays the currently selected color name


@given('Open Target Product A-90806793 page')
def open_product_page(context):
    context.driver.get('https://www.target.com/p/men-s-relaxed-fit-jeans-goodfellow-co/-/A-90806793?preselect=90509142#lnk=sametab')


@then('Verify user can click through colors')
def verify_colors(context):
    expected_colors = ['Light Wash','Dark Wash','Indigo','Tan']  # List of expected color names displayed for this product
    actual_colors = []  # List to store color names captured from the UI during the test

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # Find all available color swatches on the product page

    for c in colors:  # Click each color swatch to verify it can be selected
        c.click()

        selected_color = context.driver.find_element(*COLOR_NAMES).text  # Get the text from the variation component that shows the selected color
        selected_color = selected_color.split('\n')[1]  # Extract only the color value (ignores the label text like "Color")

        actual_colors.append(selected_color)  # Store the selected color name for later comparison
        sleep(1)

    # Verify that all expected colors are available, ignoring order
    assert set(expected_colors) == set(actual_colors), f"Expected colors: {expected_colors}, but got actual colors: {actual_colors}"