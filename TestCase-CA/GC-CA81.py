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

field_cert_serialnumber=driver.find_element(By.ID,'serialNumber')
field_cert_serialnumber.send_keys('E84C0D3289DA09E0C93F50619789FB25')
time.sleep(1) 
element_update_bttn_list = "//div[contains(text(), 'E84C0D3289DA09E0C93F50619789FB25')]"
option2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element_update_bttn_list)))
option2.click()
# Use ActionChains to simulate pressing the Tab key
action = ActionChains(driver)
action.move_to_element(option2).send_keys(Keys.TAB).perform()
action.move_to_element(option2).send_keys(Keys.ENTER).perform()
time.sleep(3)


#dropdown revoke reason
drpdwn_revoke=driver.find_element(By.CSS_SELECTOR, '.MuiFormControl-root')
drpdwn_revoke.click()
time.sleep(1)
option_1="//div[contains(text(), 'Key Compromise')]"
config_option1=wait.until(EC.element_to_be_clickable((By.XPATH, option_1)))
config_option1.click()
time.sleep(2)

btn_revoke=driver.find_element(By.CSS_SELECTOR,'button.MuiButtonBase-root:nth-child(4)')
btn_revoke.click()
time.sleep(2)

accept_btn_revoke_popup=driver.find_element(By.CSS_SELECTOR, '.swal2-confirm')
accept_btn_revoke_popup.click()
time.sleep(2)