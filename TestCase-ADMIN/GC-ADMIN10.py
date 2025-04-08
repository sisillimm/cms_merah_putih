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
driver.get(os.getenv("ADMIN_URL")) 
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
main_menu = "//span[contains(text(), 'Admin Mng.')]"
element = driver.find_element(By.XPATH, main_menu)
element.click()

menu_user_admin = "//span[contains(@class, 'MuiTypography-root') and contains(text(), 'Admin Page Master')]"
span_element = wait.until(EC.element_to_be_clickable((By.XPATH, menu_user_admin)))
span_element.click()
time.sleep(1)

#click button create
btn_create=driver.find_element(By.CSS_SELECTOR,'.css-1nlqvtm')
btn_create.click()
time.sleep(1)

#field Group Name
field_group_mastername=driver.find_element(By.ID,'masterName')
field_group_mastername.send_keys('Master Page BSSN')
time.sleep(1)

#dropdown status
drpdwn_status=driver.find_element(By.ID,'react-select-4-placeholder')
drpdwn_status.click()
config_xpath = "//div[contains(text(), 'ACTIVE')]"
config_option = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath)))
config_option.click()
time.sleep(1)

#dropdown webrights
drpdwn_webrights=driver.find_element(By.ID,'react-select-5-placeholder')
drpdwn_webrights.click()
config_xpath2 = "//div[contains(text(), 'KMS')]"
config_option2 = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath2)))
config_option2.click()
time.sleep(1)

#radiobutton link to page
radiobutton_linkpage=driver.find_element(By.CSS_SELECTOR,'label.MuiFormControlLabel-root:nth-child(2) > span:nth-child(1) > input:nth-child(1)')
radiobutton_linkpage.click()
time.sleep(1)

#field access URL
field_URL=driver.find_element(By.ID,'accessUrl')
field_URL.send_keys('/automation-dummy-page/')
time.sleep(1)

#submit button
submit_button=driver.find_element(By.CSS_SELECTOR, 'button.MuiButton-root:nth-child(2)')
submit_button.click()
time.sleep(3)
