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
driver.get(os.getenv("ADMIN_URL")) 
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
main_menu = "//span[contains(text(), 'Admin Mng.')]"
element = driver.find_element(By.XPATH, main_menu)
element.click()

menu_user_admin = "//span[contains(@class, 'MuiTypography-root') and contains(text(), 'User Admin')]"
span_element = wait.until(EC.element_to_be_clickable((By.XPATH, menu_user_admin)))
span_element.click()
time.sleep(2)

element_update_bttn_list = "//div[contains(text(), 'userval01@mail.com')]"
option2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element_update_bttn_list)))

# Click the element
option2.click()
 
# Use ActionChains to simulate pressing the Tab key
action = ActionChains(driver)
action.move_to_element(option2).send_keys(Keys.TAB).perform()
action.move_to_element(option2).send_keys(Keys.ENTER).perform()
time.sleep(2)

#field password
field_password=driver.find_element(By.ID,'password')
field_password.send_keys('12345678')
time.sleep(1)

#field confirm password
field_confirm_password=driver.find_element(By.ID,'confirmPassword')
field_confirm_password.send_keys('12345678')
time.sleep(1)

#submit
submit_button=driver.find_element(By.CSS_SELECTOR, 'button.MuiButton-root:nth-child(3)')
submit_button.click()
time.sleep(2)
