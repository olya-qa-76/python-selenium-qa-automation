from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
# driver.implicitly_wait(5)  # implicitly_wait(): checks for elements every 100 ms / applied to all find_element() and find_elements()
driver.wait = WebDriverWait(driver, 10)  # Set a maximum timeout duration (e.g., 10 seconds)


# open the url
driver.get('https://www.google.com/')

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('table')


# click search button

# 1/> wait for 4 sec
# sleep(4)
# driver.find_element(By.NAME, 'btnK').click()

# 2/> implicitly_wait():
# driver.find_element(By.NAME, 'btnK').click()

# 3/> explicit_wait():
SEARCH_BTN = (By.NAME, 'btnK')  # assigns a Selenium locator (defined by By.NAME with the value 'btnK') to a variable called search_btn.
driver.wait.until(EC.element_to_be_clickable(SEARCH_BTN), message='Search button was not clickable').click()  # wait for the element 'search_btn' until it's clickable then click on it.

# verify search results
assert 'table'.lower() in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
