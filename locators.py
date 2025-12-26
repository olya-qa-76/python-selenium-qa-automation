from selenium import webdriver
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

# open the url
driver.get('https://www.amazon.com/')

# LOCATORS
# By ID
driver.find_element(By.ID, 'twotabsearchtextbox')  # .find_element(): searches for an element,
                                                                          # throws Exception if element not found

# By XPATH
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")  # XPATH = "//tagname[@attribute = 'value']"

# By attributes, any tag
driver.find_element(By.XPATH, "//*[@aria-label='Search Amazon']")  # XPATH = "//*[@attribute = 'value']"

# By combining multiple attributes
driver.find_element(By.XPATH, "//*[@aria-label='Search Amazon' and @role='searchbox']")  # XPATH = "//tagname[@attribute1 = 'value1' and @attrubute2 = 'value2']"

# By text
driver.find_element(By.XPATH, "//*[text()='EN']")  # XPATH = "//tagname[text() = 'value']"

# By attribute, partial match
driver.find_element(By.XPATH, "//*[contains(@class, 'search-dropdown')]")  # XPATH = "//tagname[contains( @atttibute, 'value')]"

# Bad practice: using dynamically generated parts of attributes (id / class / names etc.)
driver.find_element(By.ID, 'CardInstance6ck4HI97byztr7OOJcpAZw')
driver.find_element(By.XPATH, "//*[@class='a-cardui _Zmx1a_fluidQuadImageLabel_3b-Iv']")
driver.find_element(By.XPATH, "//*[@data-csa-c-id='xw0omi-5lybao-xvl49j-jfjm3z']")

# To avoid "a-cardui _Zmx1a_,,,_3b-Iv"
driver.find_element(By.XPATH, "//*[contains(@class, 'fluidQuadImageLabel')]")

driver.quit()