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

driver=webdriver.Chrome()
driver.maximize_window()
driver.get(os.getenv("CA_URL"))
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

time.sleep(2)

# XPath targeting the span element with specific text
main_menu = "//span[contains(text(), 'Certificate Authority')]"
element = driver.find_element(By.XPATH, main_menu)
element.click()

menu_algorithm_profile = "//span[contains(@class, 'MuiTypography-root') and contains(text(), 'Algorithm Profiles')]"
span_element = wait.until(EC.element_to_be_clickable((By.XPATH, menu_algorithm_profile)))
span_element.click()
time.sleep(2)

create_btn_algorithm_profiles=driver.find_element(By.CSS_SELECTOR, '.css-mvn0cb')
create_btn_algorithm_profiles.click()
time.sleep(2)

algorithm_name=driver.find_element(By.ID, '19')
algorithm_name.send_keys('SHA1withECDSA')
time.sleep(2)

profiles_OID=driver.find_element(By.ID, '20')
profiles_OID.send_keys('BSSNECC1')
time.sleep(2)

submit_button=driver.find_element(By.CSS_SELECTOR, 'button.MuiButton-root:nth-child(2)')
submit_button.click()
time.sleep(2)