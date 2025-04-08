import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(os.getenv("CA_URL")) 
time.sleep(1)
wait = WebDriverWait(driver, 20)

emailogin=driver.find_element(By.ID, 'Email')
emailogin.send_keys(os.getenv("EMAIL"))
passwordlogin=driver.find_element(By.ID, 'Password')
passwordlogin.send_keys(os.getenv("PASSWORD"))
buttonlogin=driver.find_element(By.CLASS_NAME, 'MuiButtonBase-root')
buttonlogin.click()
time.sleep(2)

sidemenu=driver.find_element(By.CSS_SELECTOR, 'button.MuiIconButton-root:nth-child(1)')
sidemenu.click()
time.sleep(1)

# XPath targeting the span element with specific text
main_menu = "//span[contains(text(), 'Search Certificate')]"
element = driver.find_element(By.XPATH, main_menu)
element.click()
time.sleep(1)

#filter dropdown status
drpdwn_status=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(6) > div:nth-child(2) > div:nth-child(3)')
drpdwn_status.click()
time.sleep(1)
option_1="//div[contains(text(), 'Active')]"
config_option1=wait.until(EC.element_to_be_clickable((By.XPATH, option_1)))
config_option1.click()
time.sleep(3)