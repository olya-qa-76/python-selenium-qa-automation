from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-test='lp-resultsCount'] div.h-display-flex")
AD_BANNER = (By.CSS_SELECTOR, "img.heroImg")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
PRODUCT_NAME = (By.XPATH, "//div[@class='h-margin-l-default']// a")
PRODUCT_CARDS = (By.CSS_SELECTOR, "[data-test*='ProductCardVariantDefault']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "a[data-test='@web/ProductCard/title']")
PRODUCT_IMAGE = (By.CSS_SELECTOR, "[data-test*='ProductCardVariantDefault'] picture[data-test*='secondary']")


@then('Search results for {expected_product} are shown')
def verify_search_results(context, expected_product):
    actual = context.driver.wait.until(
        EC.presence_of_element_located(SEARCH_RESULTS),
        message='Search results page not found'
    ).text
    assert expected_product in actual, f"Expected: '{expected_product}' NOT in Actual: '{actual}'"


@when('Click "Add to cart" button')
def click_add_to_cart_btn(context):
    sleep(15)  # wait 15 sec for AD_BANNER to disappear
    # context.driver.wait.until(
    #     EC.invisibility_of_element_located(AD_BANNER),
    #     message='Ad Banner is still visible'
    # )
    context.driver.wait.until(
        EC.element_to_be_clickable(ADD_TO_CART_BTN),
        message='Add To Cart button is not clickable'
    ).click()


@when('Store product name')
def store_product_name(context):
    context.product = context.driver.wait.until(
        EC.presence_of_element_located(PRODUCT_NAME),
        message='Product name is not displayed'
    ).text


@when('Click Side Nav "Add to cart" button')
def click_side_nav_btn(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(SIDE_NAV_ADD_TO_CART_BTN),
        message='Add To Cart button is not clickable'
    ).click()


@then('Verify that every product on Target search results page has a title and image')
def verify_product_title_and_image(context):
    context.driver.wait.until(EC.invisibility_of_element(AD_BANNER),
        message='Ad Banner is still visible'
    )

    cards = context.driver.find_elements(*PRODUCT_CARDS)

    for card in cards:

        title = context.driver.find_elements(*PRODUCT_TITLE)
        image = context.driver.find_elements(*PRODUCT_IMAGE)

        assert title, "Product title is not visible"
        assert image, "Product image is not visible"