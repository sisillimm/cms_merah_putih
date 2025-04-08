from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

create_btn_certif_policies=driver.find_element(By.CSS_SELECTOR, '.css-mvn0cb')
create_btn_certif_policies.click()

time.sleep(2)

policy_ID_txt=driver.find_element(By.ID, '22')
policy_ID_txt.send_keys('2.16.360.1.1.1.3.35')

drop_down_certif_policies=driver.find_element(By.CSS_SELECTOR, '.css-zglcpf-control')
drop_down_certif_policies.click()
select_dowp_down = "//div[contains(text(), 'userNotice')]"
option = wait.until(EC.element_to_be_clickable((By.XPATH, select_dowp_down)))
option.click()
time.sleep(1)

qualifier_info_txt=driver.find_element(By.ID, '24')
qualifier_info_txt.send_keys('Testing Sertifikat')
time.sleep(2)

submit_button=driver.find_element(By.CSS_SELECTOR, 'button.MuiButton-root:nth-child(2)')
submit_button.click()
time.sleep(2)