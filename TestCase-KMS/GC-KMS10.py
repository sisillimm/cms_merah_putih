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

#click Key Config
menu_Key_Config = "//span[contains(@class, 'MuiTypography-root') and contains(text(), 'Key Configuration')]"
span_element = wait.until(EC.element_to_be_clickable((By.XPATH, menu_Key_Config)))
span_element.click()
time.sleep(2)

#search config key name
field_config_name = driver.find_element(By.ID,'a733fbe8-f93f-46d6-bacf-f49f4f52ff48')
field_config_name.send_keys('BSSN_ECC')
time.sleep(1)
element_update_bttn_list = "//div[contains(text(), 'BSSN_ECC')]"
option2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element_update_bttn_list)))
option2.click()
action = ActionChains(driver)
action.move_to_element(option2).send_keys(Keys.TAB).perform()
action.move_to_element(option2).send_keys(Keys.TAB).perform()
action.move_to_element(option2).send_keys(Keys.ENTER).perform()
time.sleep(2)

accept_btn_delete_popup=driver.find_element(By.CSS_SELECTOR, '.swal2-confirm')
accept_btn_delete_popup.click()
time.sleep(2)