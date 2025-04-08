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

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(os.getenv("KMS_URL")) 
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
main_menu = "//span[contains(text(), 'Key Management System')]"
element = driver.find_element(By.XPATH, main_menu)
element.click()

#click Keys Group
menu_Keys_Group = "//span[contains(@class, 'MuiTypography-root') and contains(text(), 'Keys Group')]"
span_element = wait.until(EC.element_to_be_clickable((By.XPATH, menu_Keys_Group)))
span_element.click()
time.sleep(2)

#create button
btn_create=driver.find_element(By.CSS_SELECTOR,'.css-iar8i9')
btn_create.click()
time.sleep(2)

#field Group Name
grp_name_field=driver.find_element(By.ID,'16')
grp_name_field.send_keys('Group BSSN')
time.sleep(1)

#field Group Description
grp_desc_field=driver.find_element(By.ID,'17')
grp_desc_field.send_keys('BSSN keys group')
time.sleep(1)

#field Group Issuer Name
grp_issuer_field=driver.find_element(By.ID,'18')
grp_issuer_field.send_keys('issuer BSSN')
time.sleep(1)

#submit button
submit_button=driver.find_element(By.CSS_SELECTOR, 'button.MuiButton-root:nth-child(2)')
submit_button.click()
time.sleep(4)