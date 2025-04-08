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
main_menu = "//span[contains(text(), 'Keys List')]"
element = driver.find_element(By.XPATH, main_menu)
element.click()
time.sleep(2)

field_key_name=driver.find_element(By.ID,'keysName')
field_key_name.send_keys('CA_BSSN_RSA')
time.sleep(1)
element_update_bttn_list = "//div[contains(text(), 'CA_BSSN_RSA')]"
option2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element_update_bttn_list)))
option2.click()
action = ActionChains(driver)
action.move_to_element(option2).send_keys(Keys.TAB).perform()
action.move_to_element(option2).send_keys(Keys.ENTER).perform()
time.sleep(1)

driver.execute_script("window.scrollTo(400, 2000);")
time.sleep(2)

#dropdown revoked reason
drpdwn_revoke=driver.find_element(By.CSS_SELECTOR,'.css-zglcpf-control')
drpdwn_revoke.click()
config_xpath = "//div[contains(text(), 'Key Compromise')]"
config_option = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath)))
config_option.click()
time.sleep(1)

#button revoke
btn_revoke=driver.find_element(By.CSS_SELECTOR,'button.MuiButtonBase-root:nth-child(3)')
btn_revoke.click()
time.sleep(2)

accept_btn_revoked_popup=driver.find_element(By.CSS_SELECTOR, '.swal2-confirm')
accept_btn_revoked_popup.click()
time.sleep(2)