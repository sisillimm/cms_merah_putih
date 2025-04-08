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

menu_user_admin = "//span[contains(@class, 'MuiTypography-root') and contains(text(), 'Admin Page Access')]"
span_element = wait.until(EC.element_to_be_clickable((By.XPATH, menu_user_admin)))
span_element.click()
time.sleep(1)

#click button create
btn_create=driver.find_element(By.CSS_SELECTOR,'.css-1nlqvtm')
btn_create.click()
time.sleep(2)

#field Access Group Name
field_access_groupname=driver.find_element(By.ID,'accessGroupName')
field_access_groupname.send_keys('Access Data Automation Dummy')
time.sleep(2)

#field Description
desc_field=driver.find_element(By.ID,'accessRemark')
desc_field.send_keys('Data testing Automation Access')
time.sleep(2)

#dropdown role related to(API)
drpdwn_role_related=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(4) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2)')
drpdwn_role_related.click()
time.sleep(1)
config_xpath = "//div[contains(text(), 'Admin')]"
config_option = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath)))
config_option.click()
time.sleep(1)

#click description
description=driver.find_element(By.CSS_SELECTOR,'.MuiInputBase-multiline')
description.click()
time.sleep(1)

#dropdown role for
drpdwn_role_for=driver.find_element(By.CSS_SELECTOR, 'div.MuiFormControl-root:nth-child(5) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2)')
drpdwn_role_for.click()
time.sleep(1)
config_xpath3 = "//div[contains(text(), 'KMS')]"
config_option3 = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath3)))
config_option3.click()
time.sleep(3)

#accessrole
access_read = driver.find_element(By.CSS_SELECTOR,'div.MuiGrid-container:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
access_read.click()
time.sleep(1)
access_read2 = driver.find_element(By.CSS_SELECTOR,'div.MuiGrid-container:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2)')
access_read2.click()
time.sleep(1)

driver.execute_script("window.scrollTo(100, -2000)")
time.sleep(3)

#dropdown user members
drpdwn_user_members=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(7) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2)')
drpdwn_user_members.click()
time.sleep(2)
config_xpath2 = "//div[contains(text(), 'datasisil@yopmail.com')]"
config_option2 = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath2)))
config_option2.click()
time.sleep(2)

# dropdown status
drpdwn_status=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(8) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2)')
drpdwn_status.click()
time.sleep(2)
config_xpath5 = "//div[contains(text(), 'INACTIVE')]"
config_option5 = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath5)))
config_option5.click()
time.sleep(2)

#submit button
submit_button=driver.find_element(By.CSS_SELECTOR, 'button.MuiButton-root:nth-child(2)')
submit_button.click()
time.sleep(3)
