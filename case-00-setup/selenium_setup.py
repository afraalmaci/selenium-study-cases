from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep 

service = Service("/Users/afragurcan/Desktop/Afra/drivers/chromedriver")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

page_url = ""
driver.get(page_url)
driver.maximize_window()

try:
    accept_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//div[text()='Alles accepteren']]"))
    )
    accept_btn.click()
    sleep(1)
except:
    print("Cookie popup did not appear.")

sleep(3)
driver.quit()