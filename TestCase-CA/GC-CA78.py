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
main_menu = "//span[contains(text(), 'Sign Certificate Request')]"
element = driver.find_element(By.XPATH, main_menu)
element.click()
time.sleep(1)

#dropdown certificate profile
drpdwn_crt_profile=driver.find_element(By.CSS_SELECTOR, 'div.css-amau88:nth-child(2) > div:nth-child(2) > div:nth-child(3)')
drpdwn_crt_profile.click()
time.sleep(1)
config_xpath = "//div[contains(text(), 'EXTERNAL_forCSR')]"
config_option = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath)))
config_option.click()
time.sleep(1)

#dropdown certificate algorithm
drpdwn_crt_algorithm=driver.find_element(By.ID, 'cerAlgo')
drpdwn_crt_algorithm.click()
time.sleep(1)
option_2="//div[contains(text(), 'SHA256withRSA')]"
config_option2=wait.until(EC.element_to_be_clickable((By.XPATH, option_2)))
config_option2.click()
time.sleep(2)

#field subjectname
field_subject_name_crt=driver.find_element(By.CSS_SELECTOR,'#subjectName')
field_subject_name_crt.send_keys('cn=dummyforcaexternal_bssn')
time.sleep(1)

current_folder = os.path.dirname(os.path.abspath(__file__)) 
# Create the full path to data.txt
data_txt_path = os.path.join(current_folder, "ForDataCA_External.csr")
file_input = driver.find_element(By.ID, "functionMenuName")
file_input.send_keys(data_txt_path)
time.sleep(1)


# file_input = driver.find_element(By.ID, "functionMenuName")
# file_input.send_keys('C:\CA_dummy_datades.csr')
# time.sleep(1)

submit_button=driver.find_element(By.CSS_SELECTOR, '.MuiButton-contained')
submit_button.click()
time.sleep(2)

accept_btn_importCSR_popup=driver.find_element(By.CSS_SELECTOR, '.swal2-confirm')
accept_btn_importCSR_popup.click()
time.sleep(2)

#download certificate as PEM
btn_download_PEM=driver.find_element(By.CSS_SELECTOR, 'div.MuiStack-root:nth-child(10) > button:nth-child(1)')
btn_download_PEM.click()
time.sleep(2)