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

#field Access Group Name
field_rolename=driver.find_element(By.ID,'roleName')
field_rolename.send_keys('Access Data Automation Dummy')
time.sleep(2)

element_update_bttn_list = "//div[contains(text(), 'Access Data Automation Dummy')]"
option2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element_update_bttn_list)))
option2.click()
# Use ActionChains to simulate pressing the Tab key
action = ActionChains(driver)
action.move_to_element(option2).send_keys(Keys.TAB).perform()
action.move_to_element(option2).send_keys(Keys.ENTER).perform()
time.sleep(2)

#field Description
desc_field=driver.find_element(By.ID,'accessRemark')
desc_field.send_keys(Keys.CONTROL + "a", Keys.DELETE)
desc_field.send_keys('Data testing Automation Access')
time.sleep(2)

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

#submit
submit_button=driver.find_element(By.CSS_SELECTOR, 'button.MuiButton-root:nth-child(3)')
submit_button.click()
time.sleep(2)
