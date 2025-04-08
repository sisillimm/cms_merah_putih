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
csv_file_path = 'data1.csv'
# ROOT=data1

# Read data from CSV
data_list = read_csv_data(csv_file_path)

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(os.getenv("CA_URL")) 
time.sleep(1)
wait = WebDriverWait(driver, 20)

# Assuming you're using the first row of the CSV for now
data = data_list[1]

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
