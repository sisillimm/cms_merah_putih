import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
csv_file_path = 'dataCA.csv'
# Read data from CSV
data_list = read_csv_data(csv_file_path)

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(os.getenv("CA_URL")) 
time.sleep(1)
wait = WebDriverWait(driver, 20)

# Assuming you're using the first row of the CSV for now
data = data_list[5]

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

#click CA Data
menu_CA_Data = "//span[contains(@class, 'MuiTypography-root') and contains(text(), 'CA data')]"
span_element = wait.until(EC.element_to_be_clickable((By.XPATH, menu_CA_Data)))
span_element.click()
time.sleep(1)

#click create
create_CA_data=driver.find_element(By. CSS_SELECTOR, '.css-mvn0cb')
create_CA_data.click()
time.sleep(1)

#click checkbox
xpath = "//span[contains(@class, 'MuiTypography-root') and contains(text(), 'For generating key?')]"
span_element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
span_element.click()

#click checkbox2
xpath = "//span[contains(@class, 'MuiTypography-root') and contains(text(), 'For Generating Certificate?')]"
span_element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
span_element.click()
time.sleep(1)

#issuer profile name
input_field = driver.find_element(By.ID, '41')
input_field.send_keys(data['IssuerProfileName'])
time.sleep(1)

#Issuer Key Name
input_field = driver.find_element(By.ID, '42')
input_field.send_keys(data['IssuerKeyName'])
time.sleep(1)

#crl validity
input_field = driver.find_element(By.ID, '45')
input_field.send_keys(data['CrlValidity'])
time.sleep(1)

# Dropdown AlgoProfile
dropdown = wait.until(EC.element_to_be_clickable((By.ID, '46')))
dropdown.click()
time.sleep(1)
algo_xpath = f"//div[contains(text(), '{data['AlgoProfile']}')]"
algo_option = wait.until(EC.element_to_be_clickable((By.XPATH, algo_xpath)))
algo_option.click()
time.sleep(1)

# Dropdown KeyConfigType
dropdown2 = wait.until(EC.element_to_be_clickable((By.ID, '49')))
dropdown2.click()
key_config_xpath = f"//div[contains(text(), '{data['KeyConfigType']}')]"
key_config_option = wait.until(EC.element_to_be_clickable((By.XPATH, key_config_xpath)))
key_config_option.click()
time.sleep(1)

# Dropdown ConfigProfile
dropdown4 = wait.until(EC.element_to_be_clickable((By.ID, '48')))
dropdown4.click()
config_xpath = f"//div[contains(text(), '{data['ConfigProfile']}')]"
config_option = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath)))
config_option.click()
time.sleep(1)

# Dropdown KeyGroupName
dropdown3 = wait.until(EC.element_to_be_clickable((By.ID, '50')))
dropdown3.click()
group_name_xpath = f"//div[contains(text(), '{data['KeyGroupName']}')]"
group_name_option = wait.until(EC.element_to_be_clickable((By.XPATH, group_name_xpath)))
group_name_option.click()
time.sleep(1)

# Input KeyValidity
input_field = driver.find_element(By.ID, '51')
input_field.send_keys(data['KeyValidity'])

# Input SubjectName
input_field = driver.find_element(By.ID, '52')
input_field.send_keys(data['SubjectName'])
time.sleep(1)

submit_button=driver.find_element(By.CSS_SELECTOR, 'button.MuiButton-root:nth-child(2)')
submit_button.click()
time.sleep(1)