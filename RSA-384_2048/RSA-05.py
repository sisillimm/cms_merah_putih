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

menu_name_constrains = "//span[contains(@class, 'MuiTypography-root') and contains(text(), 'Name Constrains')]"
span_element = wait.until(EC.element_to_be_clickable((By.XPATH, menu_name_constrains)))
span_element.click()
time.sleep(2)

create_btn_name_constrains=driver.find_element(By.CSS_SELECTOR, '.css-mvn0cb')
create_btn_name_constrains.click()
time.sleep(2)

name_constrains=driver.find_element(By.ID, '561')
name_constrains.send_keys('newSandbox')
time.sleep(2)

checkbox_maximum=driver.find_element(By.CSS_SELECTOR, "div.MuiFormControl-root:nth-child(4) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)")
checkbox_maximum.click()
time.sleep(2)

checkbox_minimum=driver.find_element(By.CSS_SELECTOR, "div.MuiFormControl-root:nth-child(8) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)")
checkbox_minimum.click()
time.sleep(2)

submit_button=driver.find_element(By.CSS_SELECTOR, 'button.MuiButton-root:nth-child(2)')
submit_button.click()
time.sleep(2)