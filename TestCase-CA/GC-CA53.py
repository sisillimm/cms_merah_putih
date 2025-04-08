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
csv_file_path = 'data1.csv'

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

#label key usage extended
label_key_usage_extended=driver.find_element(By.CSS_SELECTOR, 'div.MuiFormControl-root:nth-child(50) > div:nth-child(1) > label:nth-child(1)')
label_key_usage_extended.click()
time.sleep(1)

#checkbox use authority information access
checkbox_authority_information_access=driver.find_element(By.CSS_SELECTOR, 'div.MuiFormControl-root:nth-child(54) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
checkbox_authority_information_access.click()
time.sleep(1)

#checkbox issuer certificate URL
checkbox_issuer_certificate_URL=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(56) > div:nth-child(2) > label:nth-child(1) > span:nth-child(2)')
checkbox_issuer_certificate_URL.click()
time.sleep(1)

#field issuer certificate URL
field_cert_url=driver.find_element(By.ID,'453') 
field_cert_url.send_keys(Keys.CONTROL + "a", Keys.DELETE)
field_cert_url.send_keys('https://cert-download.unoproducts.id/camp-sandbox/crt/BSSNCA_Cert')
time.sleep(2)

#checkbox OCSP API URL
checkbox_OCSP_API_URL=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(62) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
checkbox_OCSP_API_URL.click()
time.sleep(1)

#checkbox CRL distribution point
checkbox_CRL_distribution_point=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(72) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
checkbox_CRL_distribution_point.click()
time.sleep(1)

#field CRL distribution point
field_crl_distribution_point=driver.find_element(By.ID,'456')
field_crl_distribution_point.send_keys(Keys.CONTROL + "a", Keys.DELETE)
field_crl_distribution_point.send_keys('https://cert-download.unoproducts.id/camp-sandbox/crl/BSSNCA_Cert')
time.sleep(2)

#radiobutton CA compromise
radiobutton_ca_compromise=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(80) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
radiobutton_ca_compromise.click()
time.sleep(1)

#radiobutton CRL distribution point critical
radiobutton_CRL_distribution_point=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(96) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
radiobutton_CRL_distribution_point.click()
time.sleep(1)

#checkbox certificate policies
checkbox_certif_policies=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(100) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
checkbox_certif_policies.click()
time.sleep(1)

#dropdown certificate policies
dropdown_certif_policies=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(102) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2)')
dropdown_certif_policies.click()
time.sleep(1)
config_xpath2 = "//div[contains(text(), '2.16.360.1.1.1.3.12')]"
config_option2 = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath2)))
config_option2.click()
time.sleep(2)

#checkbox key identifier critical and OCSP no revocation
checkbox_key_identifier_OCSP=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(108) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
checkbox_key_identifier_OCSP.click()
time.sleep(1)

#authority key identifier critical
checkbox_authority_key_identifier_critical=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(112) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
checkbox_authority_key_identifier_critical.click()
time.sleep(1)

#checkbox OCSP no revocation
checkbox_OCSP_no_revocation=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(116) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
checkbox_OCSP_no_revocation.click()
time.sleep(1)

#checkbox issuer alternative data
checkbox_issuer_alternative_data=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(122) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
checkbox_issuer_alternative_data.click()
time.sleep(1)

#dropdown certificate issuer for Root
dropdown_crt_root=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(124) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1)')
dropdown_crt_root.click()
time.sleep(1)
config_xpath6 = "//div[contains(text(), 'RootBSSNProfile')]"
config_option6 = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath6)))
config_option6.click()
time.sleep(2)

#checkbox subject altv name
checkbox_subject_altv_name=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(132) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
checkbox_subject_altv_name.click()
time.sleep(1)

#dropdown subject alternative name
dropdown_subject_altv_name=driver.find_element(By.ID, '462')
dropdown_subject_altv_name.click()
time.sleep(1)
config_xpath4 = "//div[contains(text(), 'DNSname BSSN Data')]"
config_option4 = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath4)))
config_option4.click()
time.sleep(2)

#checkbox subject infortmation access
checkbox_subject_information_access=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(140) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
checkbox_subject_information_access.click()
time.sleep(1)

#checkbox subject information access for timestamping
checkbox_subject_information_access_timestamping=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(142) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
checkbox_subject_information_access_timestamping.click()
time.sleep(1)

#timestamping URL
field_timestamping=driver.find_element(By.ID,'466')
field_timestamping.send_keys(data['Timestamping URL'])
time.sleep(2)

#checkbox subject information access for CA
checkbox_subject_information_access_CA=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(148) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
checkbox_subject_information_access_CA.click()
time.sleep(1)

#CA Repository URL
field_CArepositoryURL=driver.find_element(By.ID,'469')
field_CArepositoryURL.send_keys(data['CA Repository URL'])
time.sleep(2)

#checkbox use a policy constraint
checkbox_policy_constraint=driver.find_element(By.CSS_SELECTOR, 'div.MuiFormControl-root:nth-child(158) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
checkbox_policy_constraint.click()
time.sleep(1)

#require explicit policy
field_require_explicit_policy=driver.find_element(By.ID, '551')
field_require_explicit_policy.send_keys(Keys.CONTROL + "a", Keys.DELETE)
field_require_explicit_policy.send_keys(data['Require Explicit Policy'])
time.sleep(2)

#inhibit policy mapping
field_inhibit_policy_mapping=driver.find_element(By.ID, '552')
field_inhibit_policy_mapping.send_keys(Keys.CONTROL + "a", Keys.DELETE)
field_inhibit_policy_mapping.send_keys(data['Inhibit Policy Mapping'])
time.sleep(2)

#checkbox inhibit any policy
checkbox_inhibit_any_policy=driver.find_element(By.CSS_SELECTOR, 'div.MuiFormControl-root:nth-child(168) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
checkbox_inhibit_any_policy.click()
time.sleep(1)

#inhibit any policy
field_inhibit_any_policy=driver.find_element(By.ID, '556')
field_inhibit_any_policy.send_keys(Keys.CONTROL + "a", Keys.DELETE)
field_inhibit_any_policy.send_keys(data['Inhibit Any Policy'])
time.sleep(1)

#checkbox private key usage period
checkbox_private_key_usage_period=driver.find_element(By.CSS_SELECTOR, 'div.MuiFormControl-root:nth-child(172) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
checkbox_private_key_usage_period.click()
time.sleep(1)

#checkbox name constrains
checkbox_name_constrains=driver.find_element(By.CSS_SELECTOR, 'div.MuiFormControl-root:nth-child(176) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
checkbox_name_constrains.click()
time.sleep(1)

#dropdown permitted subtress name constrains
dropdown_permitted_subtress=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(178) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1)')
dropdown_permitted_subtress.click()
time.sleep(1)
config_xpath7="//div[contains(text(), 'dnsname:SandboxDummy')]"
config_option7=wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath7)))
config_option7.click()
time.sleep(1)

#dropdown exclude subtress name constrains
dropdown_exclude_subtress=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(180) > div:nth-child(2) > div:nth-child(3)')
dropdown_exclude_subtress.click()
time.sleep(2)
config_xpath8="//div[contains(text(), 'dnsname:bssn')]"
config_option8=wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath8)))
config_option8.click()
time.sleep(1)

#radiobutton name constrains
radiobutton_name_constrains=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(182) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
radiobutton_name_constrains.click()
time.sleep(1)

#checkbox policy mappings
checkbox_policy_mapping=driver.find_element(By.CSS_SELECTOR,'div.MuiFormControl-root:nth-child(186) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
checkbox_policy_mapping.click()
time.sleep(1)

#dropdown policy mappings
dropdown_policy_mapping=driver.find_element(By.ID,'573')
dropdown_policy_mapping.click()
time.sleep(1)
config_xpath5 = "//div[contains(text(), 'Policy Mappings Sandbox')]"
config_option5 = wait.until(EC.element_to_be_clickable((By.XPATH, config_xpath5)))
config_option5.click()
time.sleep(2)

#checkbox private key usage period
checkbox_private_key_usage_period=driver.find_element(By.CSS_SELECTOR, 'div.MuiFormControl-root:nth-child(194) > div:nth-child(2) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)')
checkbox_private_key_usage_period.click()
time.sleep(1)

submit_button=driver.find_element(By.CSS_SELECTOR, 'button.MuiButton-root:nth-child(2)')
submit_button.click()
time.sleep(4)