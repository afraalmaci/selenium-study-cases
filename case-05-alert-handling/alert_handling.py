from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
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
wait = WebDriverWait(driver, 5)

page_url = "https://the-internet.herokuapp.com/javascript_alerts"
driver.get(page_url)
driver.maximize_window()
accept_cookies(driver, wait)

'''
# Simple alert with OK button only
driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button').click()

WebDriverWait(driver, 5).until(EC.alert_is_present())

site_alert = Alert(driver)
site_alert.accept()

alert_result = driver.find_element(By.ID, 'result')
print(alert_result.text)
'''

'''
# Confirmation alert with OK and Cancel buttons
driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button').click()

WebDriverWait(driver, 5).until(EC.alert_is_present())

site_alert = Alert(driver)
site_alert.dismiss()  # Click Cancel

alert_result = driver.find_element(By.ID, 'result')
print(alert_result.text)
'''

# Prompt alert - enter text and accept
driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button').click()

# Wait for alert to appear
WebDriverWait(driver, 5).until(EC.alert_is_present())

# Switch to alert and send text
site_alert = Alert(driver)
site_alert.send_keys("Python")
site_alert.accept()

# Get result message
alert_result = driver.find_element(By.ID, 'result')
print(alert_result.text)

sleep(3)
driver.quit()