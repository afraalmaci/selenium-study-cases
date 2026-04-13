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

page_url = "https://en.wikipedia.org/wiki/Main_Page"
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

#Find and click the first news item in the "In the news" section
driver.find_element(By.XPATH, '//*[@id="mp-itn"]/ul/li[1]/a[1]').click()
sleep(2)
#Enter an input into the Wikipedia search bar and submit the search
search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("Artemis II")
search_box.send_keys(Keys.ENTER)
#Alternative Way (Finding "Search" button)
#driver.find_element(By.XPATH,'//*[@id="searchform"]/div/button').click()
sleep(2)
driver.quit()