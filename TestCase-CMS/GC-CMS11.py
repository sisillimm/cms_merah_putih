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
driver.get(os.getenv("SYSCONFIG_URL")) 
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
main_menu = "//span[contains(text(), 'Form Type')]"
element = driver.find_element(By.XPATH, main_menu)
element.click()

#click button create
btn_create=driver.find_element(By.CSS_SELECTOR,'.css-7g5n8u')
btn_create.click()
time.sleep(1)

#field type name
field_type_name=driver.find_element(By.ID,'typeName')
field_type_name.send_keys('Form DataBSSN')
time.sleep(1)

#dropdown Group Name
drpdwn_group_name=driver.find_element(By.CSS_SELECTOR,'div.MuiGrid-root:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(3)')
drpdwn_group_name.click()
config_xpath2 = "//div[contains(text(), 'GroupAutomation')]"
config_option2 = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath2)))
config_option2.click()
time.sleep(1)

#field Order Form
field_order_form=driver.find_element(By.ID,'formTypeOrder')
field_order_form.send_keys('2')
time.sleep(1)

#dropdown status
drpdwn_status=driver.find_element(By.CSS_SELECTOR,'div.MuiGrid-item:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(3)')
drpdwn_status.click()
config_xpath2 = "//div[contains(text(), 'INACTIVE')]"
config_option2 = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath2)))
config_option2.click()
time.sleep(2)

#submit button
submit_button=driver.find_element(By.CSS_SELECTOR, 'button.MuiButton-root:nth-child(2)')
submit_button.click()
time.sleep(2)