import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
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
csv_file_path = 'dataProfileOCSP.csv'

# Read data from CSV
data_list = read_csv_data(csv_file_path)

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(os.getenv("CA_URL")) 
time.sleep(1)
wait = WebDriverWait(driver, 20)

# Assuming you're using the first row of the CSV for now
data = data_list[0]

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

menu_root_certif_profile = "//span[contains(@class, 'MuiTypography-root') and contains(text(), 'Root Certificate Profile')]"
span_element = wait.until(EC.element_to_be_clickable((By.XPATH, menu_root_certif_profile)))
span_element.click()
time.sleep(2)

#click create
create_CA_certif_profile=driver.find_element(By. CSS_SELECTOR, '.css-mvn0cb')
create_CA_certif_profile.click()
time.sleep(2)

#certificate config name
field_crt_config_name=driver.find_element(By.ID, '390')
field_crt_config_name.send_keys(data['Certificate Config Name'])
time.sleep(2)

#dropdown version
dropdown_version = wait.until(EC.element_to_be_clickable((By.ID, '490')))
dropdown_version.click()
config_xpath = "//div[contains(text(), '3')]"
config_option = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath)))
config_option.click()
time.sleep(1)

#certificate validity in days
field_crt_validity_days=driver.find_element(By. ID, '391')
field_crt_validity_days.send_keys(data['Certificate Validity in Days'])
time.sleep(1)

#checkbox use basic constrains
checkbox_basic_constrains=driver.find_element(By.CSS_SELECTOR, 'div.MuiFormControl-root:nth-child(12) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
checkbox_basic_constrains.click()
time.sleep(1)

#radiobutton basic constraint isCA
radiobutton_basic_constraint=driver.find_element(By.CSS_SELECTOR, 'div.MuiFormControl-root:nth-child(14) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
radiobutton_basic_constraint.click()
time.sleep(1)

#radiobutton basic constrains critical
radiobutton_basic_constraint_critical=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(18) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
radiobutton_basic_constraint_critical.click()
time.sleep(1)

#checkbox key usage
checkbox_key_usage=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(22) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
checkbox_key_usage.click()
time.sleep(1)

#radiobutton 1keyusage
radiobutton_1_keyusage=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(24) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
radiobutton_1_keyusage.click()
time.sleep(1)

#radiobutton 10keyusage
radiobutton_10_keyusage=driver.find_element(By.CSS_SELECTOR, 'div.MuiFormControl-root:nth-child(42) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
radiobutton_10_keyusage.click()
time.sleep(1)

#checkbox key usage extended
checkbox_key_usage_extended=driver.find_element(By.CSS_SELECTOR, 'div.MuiFormControl-root:nth-child(46) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
checkbox_key_usage_extended.click()
time.sleep(1)

#dropdown key usage extended
dropdown_key_usage_extended=driver.find_element(By.CSS_SELECTOR, 'div.MuiFormControl-root:nth-child(48) > div:nth-child(2) > div:nth-child(3)')
dropdown_key_usage_extended.click()
time.sleep(1)
config_xpath = "//div[contains(text(), '1.2.840.113583.1.1.5-(PDF Signing)')]"
config_option = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath)))
config_option.click()
time.sleep(2)

#checkbox subject identifier critical
checkbox_subject_identifier_ceritical=driver.find_element(By.CSS_SELECTOR, 'div.MuiFormControl-root:nth-child(54) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
checkbox_subject_identifier_ceritical.click()
time.sleep(1)

#radiobutton subject key identifier critical
radiobutton_subject_key_identifier_critical=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(56) > div:nth-child(2) > label:nth-child(1) > span:nth-child(2)')
radiobutton_subject_key_identifier_critical.click()
time.sleep(1)

#checkbox OCSP No Revocation
checkbox_OCSP_No_Revocation=driver.find_element(By.CSS_SELECTOR, 'div.MuiFormControl-root:nth-child(62) > div:nth-child(2) > label:nth-child(1) > span:nth-child(2)')
checkbox_OCSP_No_Revocation.click()
time.sleep(1)

submit_button=driver.find_element(By.CSS_SELECTOR, 'button.MuiButton-root:nth-child(2)')
submit_button.click()
time.sleep(2)