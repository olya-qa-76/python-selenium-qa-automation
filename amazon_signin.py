from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


# create a new Chrome browser instance
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

# wait for 5 sec
sleep(5)

# LOCATORS
# Amazon logo
driver.find_element(By.XPATH, "//*[@aria-label='Amazon']")

# Email field
driver.find_element(By.ID, 'ap_email_login')

# Continue button
driver.find_element(By.XPATH, "//*[@class='a-button-input']")

# Conditions of use link
driver.find_element(By.XPATH, "//*[text()='Conditions of Use']")

# Privacy Notice link
driver.find_element(By.XPATH, "//*[text()='Privacy Notice']")

# Need Help link
driver.find_element(By.XPATH, "//*[contains(text(),'Need help?')]")

# Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

# Other issues with Sign-In link
driver.find_element(By.ID, 'ap-other-signin-issues-link')

# Create your Amazon account button
driver.find_element(By.ID, 'createAccountSubmit')

driver.quit()