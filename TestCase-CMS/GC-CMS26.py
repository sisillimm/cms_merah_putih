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
main_menu = "//span[contains(text(), 'Service Management')]"
element = driver.find_element(By.XPATH, main_menu)
element.click()
time.sleep(1)

#click create button
btn_create=driver.find_element(By.CSS_SELECTOR,'.css-13hr9cz')
btn_create.click()
time.sleep(1)

#field service name
field_service_name=driver.find_element(By.ID,'serviceName')
field_service_name.send_keys('Services BSSN')
time.sleep(1)

#field endpoint url
field_endpointurl=driver.find_element(By.ID,'endpointUrl')
field_endpointurl.send_keys('/services-bssn')
time.sleep(1)

#field description
field_desc=driver.find_element(By.ID,'description')
field_desc.send_keys('service management bssn')
time.sleep(1)

#dropdown status
drpdwn_status=driver.find_element(By.CSS_SELECTOR,'div.css-10m7hnd:nth-child(2) > div:nth-child(2) > div:nth-child(3)')
drpdwn_status.click()
config_xpath = "//div[contains(text(), 'INACTIVE')]"
config_option = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath)))
config_option.click()
time.sleep(1)

#dropdown main form
drpdwn_mainform=driver.find_element(By.CSS_SELECTOR,'div.css-10m7hnd:nth-child(3) > div:nth-child(2) > div:nth-child(3)')
drpdwn_mainform.click()
config_xpath2 = "//div[contains(text(), 'Form DataBSSN')]"
config_option2 = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath2)))
config_option2.click()
time.sleep(1)

#submit button
submit_button=driver.find_element(By.CSS_SELECTOR, 'button.MuiButton-root:nth-child(2)')
submit_button.click()
time.sleep(3)