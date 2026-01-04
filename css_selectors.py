from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


# create a new Chrome browser instance
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# CSS Selectors:
# By id: #id_value
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')  # same as BY.ID => driver.find_element(BY.ID, 'twotabsearchtextbox')
# Combining tag and id: tag#id_value
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')

# By class: .class
driver.find_element(By.CSS_SELECTOR, '.nav-progressive-attribute')
# By classes: .class1.class2
driver.find_element(By.CSS_SELECTOR, 'nav-progressive-attribute.nav-input')  # the order (position of class values) doesn't matter
# Combine tag + class: tag.class
driver.find_element(By.CSS_SELECTOR, 'input.nav-input.nav-progressive-attribute')

# By Attribute: [attribute='value']
driver.find_element(By.CSS_SELECTOR, "[aria-label='Search Amazon']")
# By Attributes: [attribute1='value1'][attribute2='value2']
driver.find_element(By.CSS_SELECTOR, "[aria-label='Search Amazon'][role='searchbox']")  # the order doesn't matter
# Combine tag + attribute: tag[attribute='value']
driver.find_element(By.CSS_SELECTOR, "input[aria-label='Search Amazon']")

# attr + class + id + tag: tag#id.class[attribute='value'] (recommended order)
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-input[role='searchbox']")

# Partial match (contain): *=
driver.find_element(By.CSS_SELECTOR, "[href*='customerservice']")
driver.find_element(By.CSS_SELECTOR, "[class*='partial value']")