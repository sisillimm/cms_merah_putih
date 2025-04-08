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

# Function to read data from CSV
def read_csv_data(csv_path):
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

# Path to your CSV file
csv_file_path = 'dataRoot.csv'

# Read data from CSV
data_list = read_csv_data(csv_file_path)

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(os.getenv("CA_URL")) 
time.sleep(1)
wait = WebDriverWait(driver, 20)

# Assuming you're using the first row of the CSV for now
data = data_list[7]

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
main_menu = "//span[contains(text(), 'Certificate Authority')]"
element = driver.find_element(By.XPATH, main_menu)
element.click()

#click CA Data Root
menu_CA_Data_Root = "//span[contains(@class, 'MuiTypography-root') and contains(text(), 'CA Data - Root')]"
span_element = wait.until(EC.element_to_be_clickable((By.XPATH, menu_CA_Data_Root)))
span_element.click()
time.sleep(1)

#click create
create_CA_data_root=driver.find_element(By. CSS_SELECTOR, '.css-mvn0cb')
create_CA_data_root.click()
time.sleep(2)

#root profile name
field_root_profile_name=driver.find_element(By.ID,'480')
field_root_profile_name.send_keys(data['Root Profile Name'])
time.sleep(1)

#root key name
field_root_key_name=driver.find_element(By.ID,'481')
field_root_key_name.send_keys(data['Root Key Name'])
time.sleep(1)

#CRL validity days
field_CRL_validity_days=driver.find_element(By.ID,'482')
field_CRL_validity_days.send_keys(data['CRL Validity Days'])
time.sleep(1)

#dropdown algorithm profiles
dropdown_algorithm_profile=driver.find_element(By.ID,'483')
dropdown_algorithm_profile.click()
config_xpath = "//div[contains(text(), 'SHA512withRSA')]"
config_option = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath)))
config_option.click()
time.sleep(1)

#dropdown config profile
dropdown_config_profile=driver.find_element(By.ID,'484')
dropdown_config_profile.click()
config_xpath2 = "//div[contains(text(), 'ProfileRSA_BSSN')]"
config_option2 = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath2)))
config_option2.click()
time.sleep(1)

#dropdown key config type name
dropdown_key_config_type_name=driver.find_element(By.ID,'485')
dropdown_key_config_type_name.click()
config_xpath3 = "//div[contains(text(), 'Key_RSA512_3072')]"
config_option3 = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath3)))
config_option3.click()
time.sleep(1)

#dropdown key group name
dropdown_key_group_name=driver.find_element(By.ID,'486')
dropdown_key_group_name.click()
config_xpath4 = "//div[contains(text(), 'Group BSSN')]"
config_option4 = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath4)))
config_option4.click()
time.sleep(1)

#key validity days
field_key_validity_days=driver.find_element(By.ID,'487')
field_key_validity_days.send_keys(data['Key Validity Days'])
time.sleep(1)

#certificate subject name
field_crt_subject_name=driver.find_element(By.ID,'488')
field_crt_subject_name.send_keys(data['Certificate Subject Name'])
time.sleep(1)

submit_button=driver.find_element(By.CSS_SELECTOR, 'button.MuiButton-root:nth-child(2)')
submit_button.click()
time.sleep(2)