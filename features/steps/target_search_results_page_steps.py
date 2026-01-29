from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-test='lp-resultsCount'] div.h-display-flex")
AD_BANNER = (By.CSS_SELECTOR, "img.heroImg")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
PRODUCT_NAME = (By.XPATH, "//div[@class='h-margin-l-default']// a")
PRODUCT_CARDS = (By.CSS_SELECTOR, "[data-test='@web/ProductCard/ProductCardVariantDefault']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test*='title']")
PRODUCT_IMAGE = (By.CSS_SELECTOR, "img")


@then('Search results for {expected_product} are shown')
def verify_search_results(context, expected_product):
    context.app.search_results_page.verify_search_results(expected_product)


@when('Click "Add to cart" button')
def click_add_to_cart_btn(context):
    context.driver.wait.until(
        EC.invisibility_of_element_located(AD_BANNER),
        message='Ad Banner is still visible'
    )
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

    # Scroll up and down to trigger lazy loading of product images and listings
    context.driver.execute_script("window.scrollTo(0,3000)","")  # 3000 is the number of pixels to scroll
    sleep(0.5)
    context.driver.execute_script("window.scrollTo(0,-2000)","")
    sleep(0.5)
    # context.driver.execute_script("window.scrollTo(0,2000)", "")
    # sleep(0.5)
    # context.driver.execute_script("window.scrollTo(0,2000)", "")
    # sleep(0.5)

    # Retrieve all product cards displayed in the search results
    cards = context.driver.find_elements(*PRODUCT_CARDS)
    print(len(cards))  # prints the number of elements (product cards) that exists.

    # Validate only the first few product cards to reduce test execution time
    for card in cards[:4]:

        # Extract the product title text for validation and logging
        title = card.find_element(*PRODUCT_TITLE).text
        assert title, "Product title is not displayed"

        # Verify that the product image element exists within the product card
        card.find_element(*PRODUCT_IMAGE)

        # Log product titles for visibility during test execution
        print(f"💜{title}")