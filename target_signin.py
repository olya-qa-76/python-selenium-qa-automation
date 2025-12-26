from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from target_search import expected_text, actual_text

# create a new Chrome browser instance
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get("https://www.target.com/")

# Click Account button
driver.find_element(By.XPATH, "//*[text()='Account']").click()
sleep(5)

# Click SignIn btn from side navigation
driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()
sleep(5)

# Verify:
# “Sign in or create account” text is shown
expected_txt = 'Sign in'
actual_txt = driver.find_element(By.XPATH, "//*[text()='Sign in or create account']").text

assert expected_text in actual_text, f"Expected {expected_txt} not it {actual_txt}"

# SignIn button is shown
driver.find_element(By.ID, 'login')

driver.quit()