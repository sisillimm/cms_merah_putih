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
time.sleep(1)

field_formtypename=driver.find_element(By.ID,'formTypeName')
field_formtypename.send_keys('DataBSSN')
time.sleep(1)
element_update_bttn_list = "//div[contains(text(), 'Form DataBSSN')]"
option2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element_update_bttn_list)))
option2.click()
action = ActionChains(driver)
action.move_to_element(option2).send_keys(Keys.TAB).perform()
action.move_to_element(option2).send_keys(Keys.TAB).perform()
action.move_to_element(option2).send_keys(Keys.ENTER).perform()
time.sleep(2)

#field Param System Name
field_param_system_name=driver.find_element(By.ID,'paramSystemName')
field_param_system_name.send_keys('Data002')
time.sleep(1)

#field Frontend Tittle
field_frontend_tittle=driver.find_element(By.ID,'frontendTitle')
field_frontend_tittle.send_keys('CRT Profile')
time.sleep(1)

#field Order Position
field_order_position=driver.find_element(By.ID,'orderPosition')
field_order_position.send_keys('2')
time.sleep(1)

#dropdown Field Type
drpdwn_field_type=driver.find_element(By.CSS_SELECTOR,'div.MuiGrid-root:nth-child(1) > div:nth-child(5) > div:nth-child(2) > div:nth-child(3)')
drpdwn_field_type.click()
config_xpath = "//div[contains(text(), 'Dropdown')]"
config_option = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath)))
config_option.click()
time.sleep(1)

#checkbox refer to other data?
checkbox_btn=driver.find_element(By.CSS_SELECTOR,'.MuiCheckbox-root')
checkbox_btn.click()
time.sleep(1)

#dropdown Form Menu
drpdwn_form_menu=driver.find_element(By.CSS_SELECTOR,'div.MuiBox-root:nth-child(6) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1)')
drpdwn_form_menu.click()
config_xpath2 = "//div[contains(text(), 'CA data')]"
config_option2 = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath2)))
config_option2.click()
time.sleep(2)

#dropdown Param
drpdwn_param=driver.find_element(By.CSS_SELECTOR,'div.css-10m7hnd:nth-child(3) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1)')
drpdwn_param.click()
config_xpath3 = "//div[contains(text(), 'config_profile')]"
config_option3 = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath3)))
config_option3.click()
time.sleep(2)

#radiobutton IsMandatory NO
radiobutton_mandatory=driver.find_element(By.CSS_SELECTOR,'label.MuiFormControlLabel-root:nth-child(2) > span:nth-child(1)')
radiobutton_mandatory.click()
time.sleep(1)

#dropdown status
drpdwn_status=driver.find_element(By.CSS_SELECTOR,'div.MuiGrid-item:nth-child(2) > div:nth-child(5) > div:nth-child(2) > div:nth-child(3)')
drpdwn_status.click()
config_xpath1 = "//div[contains(text(), 'ACTIVE')]"
config_option1 = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath1)))
config_option1.click()
time.sleep(1)
 
#field Default Value
field_default_value=driver.find_element(By.CSS_SELECTOR,'div.MuiGrid-item:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1)')
field_default_value.click()
action = ActionChains(driver)
action.move_to_element(field_default_value).send_keys(Keys.TAB).perform()
action.move_to_element(field_default_value).send_keys(Keys.TAB).perform()
action.move_to_element(field_default_value).send_keys(Keys.TAB).perform()
action.move_to_element(field_default_value).send_keys(Keys.TAB).perform()
action.move_to_element(field_default_value).send_keys(Keys.ENTER).perform()
time.sleep(2)

