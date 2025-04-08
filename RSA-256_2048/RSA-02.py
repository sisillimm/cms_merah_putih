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

#click create button
btn_create=driver.find_element(By.CSS_SELECTOR,'.css-iar8i9')
btn_create.click()
time.sleep(1)

#field Config Key Type
field_config_key_type=driver.find_element(By.ID,'12')
field_config_key_type.send_keys('Key_RSA256_2048')
time.sleep(1)

#dropdown Algorithm Category
drpdwn_algorithm_category=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(4) > div:nth-child(2) > div:nth-child(3)')
drpdwn_algorithm_category.click()
config_xpath = "//div[contains(text(), 'RSA')]"
config_option = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath)))
config_option.click()
time.sleep(1)

#dropdown Key Algorithm
drpdwn_key_algorithm=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(6) > div:nth-child(2) > div:nth-child(3)')
drpdwn_key_algorithm.click()
config_xpath2 = "//div[contains(text(), 'SHA256withRSA')]"
config_option2 = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath2)))
config_option2.click()
time.sleep(1)

#dropdown Key Size in Bites
drpdwn_key_size_bites=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(8) > div:nth-child(2) > div:nth-child(3)')
drpdwn_key_size_bites.click()
config_xpath3 = "//div[contains(text(), '2048')]"
config_option3 = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath3)))
config_option3.click()
time.sleep(1)

#dropdown Config Public Key Exponent
drpdwn_config_public_key=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(10) > div:nth-child(2) > div:nth-child(3)')
drpdwn_config_public_key.click()
config_xpath4 = "//div[contains(text(), '10001')]"
config_option4 = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath4)))
config_option4.click()
time.sleep(1)

submit_button=driver.find_element(By.CSS_SELECTOR, 'button.MuiButton-root:nth-child(2)')
submit_button.click()
time.sleep(3)
