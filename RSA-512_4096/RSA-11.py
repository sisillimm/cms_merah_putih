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
time.sleep(1)

sidemenu=driver.find_element(By.CSS_SELECTOR, 'button.MuiIconButton-root:nth-child(1)')
sidemenu.click()
time.sleep(1)

# XPath targeting the span element with specific text
main_menu = "//span[contains(text(), 'Certificate Authority')]"
element = driver.find_element(By.XPATH, main_menu)
element.click()
time.sleep(2)

#click CA Certificate Profile
menu_CA_certif_profile = "//span[contains(@class, 'MuiTypography-root') and contains(text(), 'CA Certificate Profile')]"
span_element = wait.until(EC.element_to_be_clickable((By.XPATH, menu_CA_certif_profile)))
span_element.click()
time.sleep(1)

#search crt profile ca
field_certif_profile_ca=driver.find_element(By.ID,'8c650779-c153-4667-893c-b2e15ed0726a')
field_certif_profile_ca.send_keys('CertRSA_CA')
time.sleep(1)
element_update_bttn_list = "//div[contains(text(), 'CertRSA_CA')]"
option2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element_update_bttn_list)))
option2.click()
 
# Use ActionChains to simulate pressing the Tab key
action = ActionChains(driver)
action.move_to_element(option2).send_keys(Keys.TAB).perform()
action.move_to_element(option2).send_keys(Keys.ENTER).perform()
time.sleep(2)

#dropdown certificate issuer for Root
dropdown_crt_root=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(124) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1)')
dropdown_crt_root.click()
time.sleep(1)
config_xpath6 = "//div[contains(text(), 'ForRSA512_4096')]"
config_option6 = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath6)))
config_option6.click()
time.sleep(2)

submit_button=driver.find_element(By.CSS_SELECTOR, 'button.MuiButton-root:nth-child(2)')
submit_button.click()
time.sleep(4)