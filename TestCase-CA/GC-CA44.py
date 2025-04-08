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
time.sleep(1)

sidemenu=driver.find_element(By.CSS_SELECTOR, 'button.MuiIconButton-root:nth-child(1)')
sidemenu.click()
time.sleep(1)

# XPath targeting the span element with specific text
main_menu = "//span[contains(text(), 'Certificate Authority')]"
element = driver.find_element(By.XPATH, main_menu)
element.click()

#click CA Data Root
menu_CA_Data_Root = "//span[contains(@class, 'MuiTypography-root') and contains(text(), 'CA Data - Root')]"
span_element = wait.until(EC.element_to_be_clickable((By.XPATH, menu_CA_Data_Root)))
span_element.click()
time.sleep(1)

field_root_profile_name = driver.find_element(By.ID,'0d8d27ca-7841-41d1-b15a-38ef095e8a90')
field_root_profile_name.send_keys('Root_CA_BSSNECC')
time.sleep(1)

element_update_bttn_list = "//div[contains(text(), 'Root_CA_BSSNECC')]"
option2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element_update_bttn_list)))
option2.click()
 
# Use ActionChains to simulate pressing the Tab key
action = ActionChains(driver)
action.move_to_element(option2).send_keys(Keys.TAB).perform()
action.move_to_element(option2).send_keys(Keys.ENTER).perform()
time.sleep(2)

#CRL validity days
field_CRL_validity_days=driver.find_element(By.ID,'482')
field_CRL_validity_days.send_keys(Keys.CONTROL + "a", Keys.DELETE)
field_CRL_validity_days.send_keys('100')
time.sleep(1)


submit_button=driver.find_element(By.CSS_SELECTOR, 'button.MuiButton-root:nth-child(2)')
submit_button.click()
time.sleep(2)