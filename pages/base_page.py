class Page:
# Base Page class that provides common Selenium actions.
# All page-specific classes inherit from this class to reuse
# browser interaction logic and keep tests clean.

    def __init__(self, driver):
        # Store the WebDriver instance so it can be used by all page methods
        self.driver = driver

    def open_url(self, url):
        # Navigate the browser to the provided URL
        self.driver.get(url)

    def find_element(self, *locator):
        # Locate and return a single web element using the given locator tuple
        return self.driver.find_element(*locator)

    def click(self, *locator):
        # Find an element using the provided locator and perform a click action
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        # Find an input field and send text to it
        self.driver.find_element(*locator).send_keys(text)