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
driver.get(os.getenv("VA_URL")) 
time.sleep(1)
wait = WebDriverWait(driver, 20)

emailogin=driver.find_element(By.ID, 'Email')
emailogin.send_keys(os.getenv("EMAIL"))
passwordlogin=driver.find_element(By.ID, 'Password')
passwordlogin.send_keys(os.getenv("PASSWORD"))
buttonlogin=driver.find_element(By.CLASS_NAME, 'MuiButtonBase-root')
buttonlogin.click()
time.sleep(1)

sidemenu=driver.find_element(By.CSS_SELECTOR, 'button.MuiIconButton-root:nth-child(1)')
sidemenu.click()
time.sleep(1)

# XPath targeting the span element with specific text
main_menu = "//span[contains(text(), 'OCSP Configuration')]"
element = driver.find_element(By.XPATH, main_menu)
element.click()

#search OCSP Data
issuer_Subj_Name=driver.find_element(By.ID,'issuerSubjectName')
issuer_Subj_Name.send_keys('OCSP_RSA384_2048')
time.sleep(1)
element_update_bttn_list = "//div[contains(text(), 'OCSP_RSA384_2048')]"
option2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element_update_bttn_list)))
option2.click()
 
# Use ActionChains to simulate pressing the Tab key
action = ActionChains(driver)
action.move_to_element(option2).send_keys(Keys.TAB).perform()
action.move_to_element(option2).send_keys(Keys.ENTER).perform()
time.sleep(2)

#OCSP Certificate Subject Name
ocsp_field = driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1)')
ocsp_field.click()
time.sleep(1)
config_xpath2 = "//div[contains(text(), 'OCSP_RSA384_3072')]"
config_option2 = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath2)))
config_option2.click()
time.sleep(2)

#update button
update_button = driver.find_element(By.CSS_SELECTOR,'button.MuiButton-root:nth-child(2)')
update_button.click()
time.sleep(2)