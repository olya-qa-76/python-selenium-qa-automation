from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


# create a new Chrome browser instance
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.targer.com/')  # .get(): opens a web page

# Search for 'tea'
driver.find_element(By.ID, 'search').send_keys('tea')  # .send_keys(): input keys into a field
driver.find_element(By.XPATH, "//*[contains(@data-test, 'SearchButton')]").click()  # .click(): clicks

# Wait for 5 sec: wait for page to load before verification
sleep(5)

# Verify results
expected_text = 'tea'
actual_text = driver.find_element(By.XPATH, "//*[@data-test='lp-resultsCount']").text  # .text: used when we verify page by text
print(actual_text)

assert expected_text in actual_text, f"Expected_text '{expected_text}' not in actual_text '{actual_text}'"
print('Test PASSED')

driver.quit()  # .quit(): exits browser