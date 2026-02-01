from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


AD_BANNER = (By.CSS_SELECTOR, "img.heroImg")
PRODUCT_NAME = (By.XPATH, "//div[@class='h-margin-l-default']// a")
PRODUCT_CARDS = (By.CSS_SELECTOR, "[data-test='@web/ProductCard/ProductCardVariantDefault']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test*='title']")
PRODUCT_IMAGE = (By.CSS_SELECTOR, "img")


@then('Search results for {expected_product} are shown')
def verify_search_results(context, expected_product):
    context.app.search_results_page.verify_search_results(expected_product)


@when('Click "Add to cart" button')
def click_add_to_cart_btn(context):
    context.app.search_results_page.click_add_to_cart_btn()


@when('Store product name')
def store_product_name(context):
    context.product = context.driver.wait.until(
        EC.presence_of_element_located(PRODUCT_NAME),
        message='Product name is not displayed'
    ).text


@when('Click Side Nav "Add to cart" button')
def click_side_nav_sign_in_btn(context):
    context.app.search_results_page.click_side_nav_add_to_cart_btn()


@then('Verify that every product on Target search results page has a title and image')
def verify_product_title_and_image(context):
    context.driver.wait.until(EC.invisibility_of_element(AD_BANNER),
        message='Ad Banner is still visible'
    )

    context.driver.execute_script("window.scrollTo(0,3000)","")
    sleep(0.5)
    context.driver.execute_script("window.scrollTo(0,2000)","")
    sleep(0.5)
    cards = context.driver.find_elements(*PRODUCT_CARDS)
    print(len(cards))

    for card in cards[:4]:

        title = card.find_element(*PRODUCT_TITLE).text
        assert title, "Product title is not displayed"

        card.find_element(*PRODUCT_IMAGE)

        print(f"💜{title}")