from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep 

def accept_cookies(driver, wait):
    """Handle cookie acceptance popup"""
    try:
        accept_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//div[text()='Alles accepteren']]"))
        )
        accept_btn.click()
        sleep(1)
    except:
        print("Cookie popup did not appear.")


service = Service("/Users/afragurcan/Desktop/Afra/drivers/chromedriver")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 3)

page_url = "https://the-internet.herokuapp.com/upload"
driver.get(page_url)
driver.maximize_window()

accept_cookies(driver, wait)

# Wait for file upload input to be present
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'file-upload')))

# Find file upload element and send file path
file_upload = driver.find_element(By.ID, 'file-upload')
file_path = '/Users/afragurcan/Downloads/invalid-format.txt'
file_upload.send_keys(file_path)

# Click submit button
driver.find_element(By.ID, 'file-submit').click()

# Wait for result message to appear
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/h3')))

# Get and print result
result = driver.find_element(By.XPATH, '//*[@id="content"]/div/h3')
print(result.text)

sleep(3)
driver.quit()