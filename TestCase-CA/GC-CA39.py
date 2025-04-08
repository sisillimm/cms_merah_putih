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

time.sleep(1)

sidemenu=driver.find_element(By.CSS_SELECTOR, 'button.MuiIconButton-root:nth-child(1)')
sidemenu.click()

time.sleep(1)

# XPath targeting the span element with specific text
main_menu = "//span[contains(text(), 'Certificate Authority')]"
element = driver.find_element(By.XPATH, main_menu)
element.click()

menu_root_certif_profile = "//span[contains(@class, 'MuiTypography-root') and contains(text(), 'Root Certificate Profile')]"
span_element = wait.until(EC.element_to_be_clickable((By.XPATH, menu_root_certif_profile)))
span_element.click()
time.sleep(1)

filter_crt_validity_days=driver.find_element(By.ID, 'df027566-4a6c-4559-8315-75fe1f2e1cff')
filter_crt_validity_days.send_keys('3')
time.sleep(2)
