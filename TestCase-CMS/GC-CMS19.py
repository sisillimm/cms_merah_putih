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
main_menu = "//span[contains(text(), 'Form Type')]"
element = driver.find_element(By.XPATH, main_menu)
element.click()
time.sleep(1)

field_formtypename=driver.find_element(By.ID,'formTypeName')
field_formtypename.send_keys('DataBSSN')
time.sleep(1)
element_update_bttn_list = "//div[contains(text(), 'Form DataBSSN')]"
option2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element_update_bttn_list)))

# Click the element
option2.click()
 
# Use ActionChains to simulate pressing the Tab key
action = ActionChains(driver)
action.move_to_element(option2).send_keys(Keys.TAB).perform()
action.move_to_element(option2).send_keys(Keys.TAB).perform()
action.move_to_element(option2).send_keys(Keys.ENTER).perform()
time.sleep(2)

element_param_update = "//div[contains(text(), 'Data004')]"
option2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element_param_update)))
option2.click()
 
# Use ActionChains to simulate pressing the Tab key
action = ActionChains(driver)
action.move_to_element(option2).send_keys(Keys.TAB).perform()
action.move_to_element(option2).send_keys(Keys.ENTER).perform()
time.sleep(2)

#dropdown status
drpdwn_status=driver.find_element(By.CSS_SELECTOR,'div.MuiGrid-item:nth-child(2) > div:nth-child(5) > div:nth-child(2) > div:nth-child(3)')
drpdwn_status.click()
config_xpath1 = "//div[contains(text(), 'INACTIVE')]"
config_option1 = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath1)))
config_option1.click()
time.sleep(1)
 
#submit button
submit_button=driver.find_element(By.CSS_SELECTOR, 'button.MuiButton-root:nth-child(2)')
submit_button.click()
time.sleep(2)

