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

menu_user_admin = "//span[contains(@class, 'MuiTypography-root') and contains(text(), 'User Admin')]"
span_element = wait.until(EC.element_to_be_clickable((By.XPATH, menu_user_admin)))
span_element.click()
time.sleep(2)

#click create button
btn_create=driver.find_element(By.CSS_SELECTOR,'.css-1nlqvtm')
btn_create.click()
time.sleep(1)

#field firstname
field_firstname=driver.find_element(By.ID,'firstName')
field_firstname.send_keys('User')
time.sleep(1)

#field lastname
field_lastname=driver.find_element(By.ID,'lastName')
field_lastname.send_keys('BSSN')
time.sleep(1)

#field email
field_email=driver.find_element(By.ID,'email')
field_email.send_keys('userbssn@yopmail.com')
time.sleep(1)

#field mobile phone
field_mobilephone=driver.find_element(By.ID,'mobile')
field_mobilephone.send_keys('081829373900')
time.sleep(1)

#field password
field_password=driver.find_element(By.ID,'password')
field_password.send_keys('Bssn123!')
time.sleep(1)

#field confirm password
field_confirm_password=driver.find_element(By.ID,'confirmPassword')
field_confirm_password.send_keys('Bssn123!')
time.sleep(1)

#dropdown status
drpdwn_status=driver.find_element(By.CSS_SELECTOR,'#react-select-4-placeholder')
drpdwn_status.click()
config_xpath = "//div[contains(text(), 'INACTIVE')]"
config_option = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath)))
config_option.click()
time.sleep(1)

#access group
access_group = driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(9) > div:nth-child(2) > div:nth-child(3)')
access_group.click()
config_xpath2 = "//div[contains(text(), 'Administrator 1')]"
config_option2 = wait.until(EC.element_to_be_clickable((By.XPATH,config_xpath2)))
config_option2.click()
time.sleep(2)

#submit
submit_button=driver.find_element(By.CSS_SELECTOR, 'button.MuiButton-root:nth-child(2)')
submit_button.click()
time.sleep(2)