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

menu_subject_alternative = "//span[contains(@class, 'MuiTypography-root') and contains(text(), 'Subject Alternative Names')]"
span_element = wait.until(EC.element_to_be_clickable((By.XPATH, menu_subject_alternative)))
span_element.click()
time.sleep(2)

create_btn_subject_altv=driver.find_element(By.CSS_SELECTOR, '.css-mvn0cb')
create_btn_subject_altv.click()
time.sleep(2)

name_label=driver.find_element(By.ID, '420')
name_label.send_keys('For BSSN')
time.sleep(2)

drop_down_altv_name_type=driver.find_element(By.CSS_SELECTOR, 'div.MuiFormControl-root:nth-child(4) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2)')
drop_down_altv_name_type.click()
select_dowp_down = "//div[contains(text(), 'dNSName')]"
option = wait.until(EC.element_to_be_clickable((By.XPATH, select_dowp_down)))
option.click()
time.sleep(1)

name_OID=driver.find_element(By.CSS_SELECTOR, 'div.MuiFormControl-root:nth-child(6) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1)')
name_OID.click()
select_name_OID="//div[contains(text(), '1.3.6.1.5.5.7.8.6')]"
option2=wait.until(EC.element_to_be_clickable((By.XPATH,select_name_OID)))
option2.click()
time.sleep(2)

name_data_altv=driver.find_element(By.ID, '421')
name_data_altv.send_keys('cmp-web-ca.unoproducts.id')
time.sleep(2)

submit_button=driver.find_element(By.CSS_SELECTOR, 'button.MuiButton-root:nth-child(2)')
submit_button.click()
time.sleep(2)
