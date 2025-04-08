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
data = data_list[3]

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
time.sleep(2)

#click CA Certificate Profile
menu_CA_certif_profile = "//span[contains(@class, 'MuiTypography-root') and contains(text(), 'CA Certificate Profile')]"
span_element = wait.until(EC.element_to_be_clickable((By.XPATH, menu_CA_certif_profile)))
span_element.click()
time.sleep(1)

#click create
create_CA_certif_profile=driver.find_element(By. CSS_SELECTOR, '.css-mvn0cb')
create_CA_certif_profile.click()
time.sleep(1)

#certificate config name
field_crt_config_name=driver.find_element(By.ID, '435')
field_crt_config_name.send_keys(data['Certificate Config Name'])
time.sleep(1)

#certificate validity in days
field_crt_validity_days=driver.find_element(By. ID, '436')
field_crt_validity_days.send_keys(data['Certificate Validity in Days'])
time.sleep(1)

#dropdown version
dropdown_version = wait.until(EC.element_to_be_clickable((By.ID, '491')))
dropdown_version.click()
config_xpath = "//div[contains(text(), '3')]"
config_option = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath)))
config_option.click()
time.sleep(1)

#checkbox use basic constrains
checkbox_basic_constrains=driver.find_element(By.CSS_SELECTOR, 'div.MuiFormControl-root:nth-child(12) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
checkbox_basic_constrains.click()
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

#dropdown certificate issuer for Root
dropdown_crt_root=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(124) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1)')
dropdown_crt_root.click()
time.sleep(1)
config_xpath6 = "//div[contains(text(), 'RootECDSA_OCSP')]"
config_option6 = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath6)))
config_option6.click()
time.sleep(2)

submit_button=driver.find_element(By.CSS_SELECTOR, 'button.MuiButton-root:nth-child(2)')
submit_button.click()
time.sleep(4)