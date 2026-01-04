from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()


# Open stackoverflow signup page
driver.get('https://stackoverflow.com/users/signup')

# Locate "Create your account" text:
driver.find_element(By.XPATH, "//h1[text()='Create your account']")

# Locate "terms of service" text:
driver.find_element(By.CSS_SELECTOR, "div.fs-caption")

# Locate "Email" field:
driver.find_element(By.ID, 'email')

# Locate "Password" field:
driver.find_element(By.ID, 'password')

# Locate "Show Password" icon:
driver.find_element(By.CSS_SELECTOR, ".js-show-password")

# Locate "Sign Up" button:
driver.find_element(By.ID, "submit-button")

# Locate "Sign up with Google" button:
driver.find_element(By.CSS_SELECTOR, "#openid-buttons .s-btn__google")

# Locate "Sign up with GitHub" button:
driver.find_element(By.CSS_SELECTOR, "#openid-buttons .s-btn__github")

# Locate "Get Stack Overflow Internal free for up to 50 users." link:
driver.find_element(By.XPATH, "//*[text()='Get Stack Overflow Internal free for up to 50 users']")