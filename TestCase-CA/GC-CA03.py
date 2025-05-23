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

menu_certif_policies = "//span[contains(@class, 'MuiTypography-root') and contains(text(), 'Certificate Policies')]"
span_element = wait.until(EC.element_to_be_clickable((By.XPATH, menu_certif_policies)))
span_element.click()
time.sleep(2)

element_update_bttn_list = "//div[contains(text(), 'Sertifikat')]"
option2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element_update_bttn_list)))
option2.click()
 
# Use ActionChains to simulate pressing the Tab key
action = ActionChains(driver)
action.move_to_element(option2).send_keys(Keys.TAB).perform()
action.move_to_element(option2).send_keys(Keys.ENTER).perform()
time.sleep(2)

qualifier_info_txt=driver.find_element(By.ID, '24')
qualifier_info_txt.send_keys(Keys.CONTROL + "a", Keys.DELETE)
qualifier_info_txt.send_keys('Data BSSN Sertifikat')
time.sleep(1)

update_btn_form=driver.find_element(By.CSS_SELECTOR, 'button.MuiButton-root:nth-child(2)')
update_btn_form.click()
time.sleep(3)