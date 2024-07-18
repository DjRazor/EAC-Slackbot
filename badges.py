# Automation for ID Badge Requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import os
import sys

import pandas as pd
import pyautogui as pag

import time
from datetime import datetime, timedelta

# Email constants (change if needed)
email_recipient = "crdunc@byu.edu" # CHANGE BACK
email_subject = "McKay EPP ID Badge Request"
email_message = "Here is an excel sheet of badges we need. Thank you!"

def main(username, password, email):
    print(f'Running badges script with {username}, {password}, {email}')

    # Set up starting directory
    current_path = os.getcwd()

    # Set up the download directory
    download_dir = os.path.join(os.getcwd(), "downloads")

    # Create the download directory if it doesn't exist
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    if current_path != download_dir:
        # Change the working directory to the desired path
        os.chdir(download_dir)
        print(f"Changed working directory to: {download_dir}")
    else:
        print("Currently in needed directory")

    # # Set up Chrome options
    # chrome_options = webdriver.ChromeOptions()
    # prefs = {"download.default_directory": download_dir}
    # chrome_options.add_experimental_option("prefs", prefs)
    # chrome_options.add_argument("--start-maximized")

    # # Set up the WebDriver
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    # wait = WebDriverWait(driver, 30)

    # # Set up date (3 months ago)
    # curr_time = datetime.now()
    # week_ago = curr_time - timedelta(weeks=12)
    # mod_month = str(week_ago.month).zfill(2)
    # mod_curr_month = str(curr_time.month).zfill(2)
    # mod_curr_day = str(curr_time.day).zfill(2)
    # three_months_ago = f">{week_ago.month}/{week_ago.day}/{week_ago.year}"

    # try:
    #     # Navigate to MAS
    #     print("Navigating to MAS...")
    #     driver.get("https://mas.byu.edu/#/")

    #     # Login to MAS
    #     username_box = driver.find_element(By.NAME, "username")
    #     username_box.send_keys(username) # Insert NetID here
    #     password_box = driver.find_element(By.NAME, "password")
    #     password_box.send_keys(password) # Insert password here
    #     sign_in_button = driver.find_element(By.ID, "byuSignInButton")
    #     sign_in_button.click()

    #     try:
    #         wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="trust-browser-button"]')))
    #         duo_button = driver.find_element(By.XPATH, '//*[@id="trust-browser-button"]')
    #         duo_button.click()
    #     except:
    #         print("*** DUO push timeout error occured. Run script again. ***")

    #     # Generate Report
    #     wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Fingerprinting")))
    #     fp_link = driver.find_element(By.LINK_TEXT, "Fingerprinting")
    #     fp_link.click()

    #     wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="notes-column"]/div[1]/div[1]/button[1]')))
    #     search_button = driver.find_element(By.XPATH, '//*[@id="notes-column"]/div[1]/div[1]/button[1]')
    #     search_button.click()

    #     wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="DesignationPanel"]/div/div/div/span/span[1]/span/ul/li/input')))
    #     standing = driver.find_element(By.XPATH, '//*[@id="DesignationPanel"]/div/div/div/span/span[1]/span/ul/li/input')
    #     standing.send_keys("Student (5 Years)")
    #     standing.send_keys(Keys.ENTER)
    #     time.sleep(2)

    #     date_sent = driver.find_element(By.XPATH, '//*[@id="SubmissionPanel"]/div/div/div/div[1]/div[1]/div/div/input')
    #     date_sent.send_keys(three_months_ago)
    #     time.sleep(1)

    #     clear_date = driver.find_element(By.XPATH, '//*[@id="SubmissionPanel"]/div/div/div/div[1]/div[2]/div/div/input')
    #     clear_date.send_keys(three_months_ago)
    #     time.sleep(1)

    #     id_date = driver.find_element(By.XPATH, '//*[@id="SubmissionPanel"]/div/div/div/div[2]/div[3]/div/div/input')
    #     id_date.send_keys("=")
    #     time.sleep(1)
    #     id_date.send_keys(Keys.ENTER)

    #     wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="notes-column"]/div[1]/div[5]/button')))
    #     view_reports = driver.find_element(By.XPATH, '//*[@id="notes-column"]/div[1]/div[5]/button')
    #     view_reports.click()

    #     wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.select2-container')))
    #     select_element = driver.find_element(By.CSS_SELECTOR, '.select2-container')
    #     select_element.click()
        
    #     wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.select2-search__field')))
    #     search_bar = driver.find_element(By.CSS_SELECTOR, '.select2-search__field')
    #     time.sleep(1)
    #     search_bar.send_keys("byu id")
    #     time.sleep(0.2)
    #     search_bar.send_keys(Keys.ENTER)
    #     time.sleep(0.2)
    #     search_bar.send_keys("cactus id")
    #     time.sleep(0.2)
    #     search_bar.send_keys(Keys.ENTER)
    #     time.sleep(0.2)
    #     search_bar.send_keys("fp cleared")
    #     time.sleep(0.2)
    #     search_bar.send_keys(Keys.ENTER)
    #     time.sleep(0.2)
    #     generate_report = driver.find_element(By.CSS_SELECTOR, '.btn.ml-sm.btn-success')
    #     generate_report.click()
    #     time.sleep(1.5)
    #     download_report = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[2]/div/button[3]')
    #     driver.execute_script("arguments[0].click();", download_report)
    #     print("Downloading MAS Report...")
    #     time.sleep(4)

    #     # Get the list of all files in the download directory
    #     files = [os.path.join(download_dir, f) for f in os.listdir(download_dir)]

    #     # Check if there are any files in the directory
    #     if not files:
    #         raise FileNotFoundError("No files found in the download directory.")

    #     # Get the most recently added file (using creation time)
    #     most_recent_file = max(files, key=os.path.getctime)

    #     # Check if the most recent file is a CSV
    #     if most_recent_file.endswith('.csv'):
    #         # Display the first few rows of the DataFrame
    #         print("Downloaded MAS report:", os.path.basename(most_recent_file))
    #     else:
    #         print(f"The most recent file is not a CSV file: {most_recent_file}")

    #     # Read the CSV file with Pandas
    #     df = pd.read_csv(most_recent_file)
    #     first_fp_date = df['FP  1 Fingerprint Date FP Cleared']

    #     if 'FP  2 Fingerprint Date FP Cleared' in df.columns:
    #         print("Found 2nd date")
    #         second_fp_date = df['FP  2 Fingerprint Date FP Cleared'].notna()
    #         df.loc[second_fp_date, 'FP  1 Fingerprint Date FP Cleared'] = df.loc[second_fp_date, 'FP  2 Fingerprint Date FP Cleared']
    #         df.drop('FP  2 Fingerprint Date FP Cleared', axis=1, inplace=True)
    #     if 'FP  3 Fingerprint Date FP Cleared' in df.columns:
    #         print("Found 3rd date")
    #         third_fp_date = df['FP  3 Fingerprint Date FP Cleared'].notna()
    #         df.loc[third_fp_date, 'FP  1 Fingerprint Date FP Cleared'] = df.loc[third_fp_date, 'FP  3 Fingerprint Date FP Cleared']
    #         df.drop('FP  3 Fingerprint Date FP Cleared', axis=1, inplace=True)

    #     df = df.set_axis(['BYU ID', 'Cactus ID', 'Exp. Date'], axis=1)
    #     df['BYU ID'] = df['BYU ID'].astype(str).str.zfill(9) # Adds leading 0's to BYU ID's that need it
    #     byu_id_data = df['BYU ID']

    #     # Navigate to AIM and verify pic presence
    #     print("Navigating to AIM...")
    #     driver.get("https://y.byu.edu/ry/ae/prod/person/cgi/personSummary.cgi")

    #     wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/ul/li[9]/a')))
    #     id_card_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/ul/li[9]/a')
    #     id_card_button.click()

    #     missing_pic_ids = []
    #     for id in byu_id_data:
    #         wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="Content"]/form/table/tbody/tr/td/table/tbody/tr/td[1]/input[1]')))
    #         aim_search = driver.find_element(By.XPATH, '//*[@id="Content"]/form/table/tbody/tr/td/table/tbody/tr/td[1]/input[1]')
    #         aim_search.send_keys(id)
    #         aim_search.send_keys(Keys.ENTER)
    #         time.sleep(3)
            
    #         try:
    #             WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.error')))
    #             print("MISSING ID CARD/PICTURE:", id)
    #             missing_pic_ids.append(id)
    #         except:
    #             print("ID card found for:", id)

    #     # Remove BYU ID's from excel sheet that don't have ID Card's
    #     for id in missing_pic_ids:
    #         row_with_id = df['BYU ID'] == id
    #         df = df[~row_with_id]
    #     df = df.reset_index(drop=True)

    #     # Change Exp Date to reflect proper year
    #     df['Exp. Date'] = pd.to_datetime(df['Exp. Date'])
    #     df['Exp. Date'] = df['Exp. Date'].apply(lambda x: x.replace(year=curr_time.year + 5))
    #     df['Exp. Date'] = df['Exp. Date'].dt.month.astype(str) + '/' + df['Exp. Date'].dt.day.astype(str) + df['Exp. Date'].dt.strftime('/%Y')

    #     print("Updated File:")
    #     print(df.head())

    #     # Rename and save file
    #     name_const = "ID Badge Request"
    #     new_name = f"{curr_time.year}-{mod_curr_month}-{mod_curr_day} {name_const}.xlsx"
    #     directory_name = os.path.dirname(most_recent_file)
    #     try:
    #         new_dir = os.path.join(directory_name, new_name)
    #         os.rename(most_recent_file, new_dir)
    #         df.to_excel(new_dir, index=False)
    #     except:
    #         print("*** There is a file with a duplicate name that exists in the same folder.\nDelete it, and rerun this program. ***")
    #         driver.quit()

    #     # Send Email in Outlook
    #     print("Navigating to Outlook to send email...")

    #     try:
    #         driver.get(f"https://outlook.office.com/mail/{email}/")
    #     except:
    #         print("Invalid email. Please try again.")
    #         driver.quit()
    #         return "Invalid email... Please try again."

    #     wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="i0116"]')))
    #     sign_in = driver.find_element(By.XPATH, '//*[@id="i0116"]')
    #     sign_in.send_keys(username)
    #     sign_in.send_keys("@byu.edu")
    #     sign_in.send_keys(Keys.ENTER)

    #     wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="i0118"]')))
    #     password_box = driver.find_element(By.XPATH, '//*[@id="i0118"]')
    #     password_box.send_keys(password)
    #     password_box.send_keys(Keys.ENTER)

    #     try:
    #         wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="idSIButton9"]')))
    #         yes_button = driver.find_element(By.XPATH, '//*[@id="idSIButton9"]')
    #         yes_button.click()
    #     except:
    #         print("*** DUO push timeout error occured. Run script again. ***")

    #     wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="114-group"]/div/div[1]/div/div/span/button[1]')))
    #     new_mail = driver.find_element(By.XPATH, '//*[@id="114-group"]/div/div[1]/div/div/span/button[1]')
    #     new_mail.click()

    #     wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="docking_InitVisiblePart_0"]/div/div[3]/div[1]/div/div[4]/div/div/div[1]')))
    #     to = driver.find_element(By.XPATH, '//*[@id="docking_InitVisiblePart_0"]/div/div[3]/div[1]/div/div[4]/div/div/div[1]')
    #     to.send_keys(email_recipient)
    #     time.sleep(2)
        
    #     wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Add a subject"]')))
    #     subject = driver.find_element(By.XPATH, '//input[@placeholder="Add a subject"]')
    #     subject.send_keys(email_subject)
        
    #     message_box = driver.find_element(By.XPATH, '//div[contains(@class, "elementToProof")]')
    #     message_box.send_keys(email_message)

    #     insert_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/div/div/div/span/div[1]/div/div/div[5]/div/button')
    #     insert_button.click()
        
    #     wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/button')))
    #     attach = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/button')
    #     attach.click()

    #     wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div/ul/li[1]/div/ul/li[2]/button')))
    #     onedrive = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div/div/div/div/div/ul/li[1]/div/ul/li[2]/button')
    #     onedrive.click()

    #     wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[2]')))
    #     files_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[2]')
    #     files_button.click()

    #     wait.until(EC.visibility_of_element_located((By.XPATH, '//span[contains(text(), "downloads")]')))
    #     downloads = driver.find_element(By.XPATH, '//span[contains(text(), "downloads")]')
    #     action = ActionChains(driver)
    #     action.double_click(downloads).perform()

    #     wait.until(EC.visibility_of_element_located((By.XPATH, f'//span[contains(text(), "{new_name}")]')))
    #     select_file = driver.find_element(By.XPATH, f'//span[contains(text(), "{new_name}")]')
    #     select_file.click()
    #     time.sleep(0.5)

    #     dropdown = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div/div/div/span/button[2]')
    #     dropdown.click()
    #     time.sleep(0.5)

    #     attach_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[5]/div/div/div/div/div/div/ul/li[2]/button')
    #     attach_button.click()

    #     time.sleep(8)
        
    #     send = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div/div/div/div[3]/div/div/div[3]/div[1]/div/div/div/div[2]/div[1]/div/span/button[1]')
    #     send.click()
    #     print("Sent email to ID Center successfully.")
    #     time.sleep(4)

    #     # Upload excel sheet to Box (UPDATE IF NEW YEAR)
    #     driver.get("https://byu.app.box.com/folder/267227390320")

    #     wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[1]/form/button')))
    #     continue_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div/div[1]/form/button')
    #     continue_button.click()

    #     wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[6]/span/div/div[2]/main/div/div/div[1]/div/div[2]/div/div/span[2]/span[3]/div/button')))
    #     new_file = driver.find_element(By.XPATH, '/html/body/div[2]/div[6]/span/div/div[2]/main/div/div/div[1]/div/div[2]/div/div/span[2]/span[3]/div/button')
    #     new_file.click()

    #     wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/ul/div/div[2]/div/li[1]')))
    #     upload = driver.find_element(By.XPATH, '/html/body/div[5]/ul/div/div[2]/div/li[1]')
    #     upload.click()

    #     time.sleep(3)
    #     path_for_sheet = f"{download_dir}\\{new_name}"
    #     pag.write(path_for_sheet)
    #     pag.press('enter')
    #     print("Uploaded ID Badge Request file to Box.")
    #     time.sleep(5)

    #     # Update MAS profiles and send emails
    #     driver.get("https://mas.byu.edu/#/")
    #     wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Fingerprinting")))
    #     fp_link = driver.find_element(By.LINK_TEXT, "Fingerprinting")
    #     fp_link.click()

    #     valid_ids = df['BYU ID']
        
    #     for id in valid_ids:
    #         try:
    #             # Update ID Card Date
    #             wait.until(EC.presence_of_element_located((By.ID, "vue-student-search")))
    #             search_box = driver.find_element(By.NAME, "student-search")
    #             search_box.clear()
    #             search_box.send_keys(id)
    #             time.sleep(1)
    #             search_box.send_keys(Keys.ENTER)

    #             for i in range(1, 4):
    #                 x = 5 - i
    #                 try:
    #                     WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, f'/html/body/div[1]/div/div/section/div/article/div[2]/div/div/div/div[2]/div[5]/div[2]/div[2]/div/div/div[{x}]/div/div/div[2]/div/div/div/div[2]/div[3]/div/div/input')))
    #                     temp_bill_box = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div/section/div/article/div[2]/div/div/div/div[2]/div[5]/div[2]/div[2]/div/div/div[{x}]/div/div/div[2]/div/div/div/div[2]/div[3]/div/div/input')
    #                     time.sleep(1)
    #                     temp_bill_box.send_keys(mod_curr_month)
    #                     time.sleep(1)
    #                     temp_bill_box.send_keys(mod_curr_day)
    #                     time.sleep(1)
    #                     temp_bill_box.send_keys(curr_time.year)
    #                     time.sleep(1)
    #                     temp_bill_box.send_keys(Keys.ENTER)
    #                     time.sleep(1)
    #                     print("Found and updated ID Card Date box for", id)
    #                     break
    #                 except:
    #                     print("Searching for ID Card Date box...")
                
    #             # Send email
    #             wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/section/div/article/div[2]/div/div/div/div[2]/div[5]/div[2]/div[2]/div/div/div[3]/span')))
    #             time.sleep(1)
    #             email_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/section/div/article/div[2]/div/div/div/div[2]/div[5]/div[2]/div[2]/div/div/div[3]/span')
    #             email_button.click()

    #             wait.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(text(), "Send To School Email")]')))
    #             send_email = driver.find_element(By.XPATH, '//button[contains(text(), "Send To School Email")]')
    #             time.sleep(4)
    #             send_email.click()

    #             time.sleep(2)
    #             alert = driver.switch_to.alert
    #             alert.accept()
    #             driver.switch_to.default_content()

    #             # Update notes section
    #             wait.until(EC.visibility_of_element_located((By.ID, "new-note-button")))
    #             add_note = driver.find_element(By.ID, "new-note-button")
    #             time.sleep(2)
    #             add_note.click()

    #             wait.until(EC.visibility_of_element_located((By.ID, "new-note-text")))
    #             note = driver.find_element(By.ID, "new-note-text")
    #             time.sleep(0.5)
    #             note.send_keys("Sent FP Clearance + EPP Card Letter.")
            
    #             wait.until(EC.visibility_of_element_located((By.ID, "new-note-submit")))
    #             save = driver.find_element(By.ID, "new-note-submit")
    #             time.sleep(0.5)
    #             save.click()
    #             time.sleep(0.5)

    #         except:
    #             print("*** Error with", id, "MAS profile, double check status ***")

    #     print("Updated MAS profiles.")

    #     try:
    #         if os.path.exists(path_for_sheet):
    #             os.remove(path_for_sheet)
    #             print(f"{path_for_sheet} has been successfully deleted to maximize storage.")
    #         else:
    #             print(f"{path_for_sheet} does not exist. It may have been deleted already.")
    #     except Exception as e:
    #         print(f"An error occurred while deleting file from OneDrive: {e}")    

    #     # Reached the end
    #     print("Successfully completed ID Badge Request!")
    #     time.sleep(10)

    # finally:
    #     # Close the driver
    #     driver.quit()

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
