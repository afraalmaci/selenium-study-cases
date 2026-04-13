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

page_url = "https://store.steampowered.com/charts/topselling/NL"
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

#for first element
game_name = driver.find_element(By.CLASS_NAME,"_1n_4-zvf0n4aqGEksbgW9N").text
print(f"Game name -> {game_name}")

#for all elements that have same class name
#game_names -> a list
game_names = driver.find_elements(By.CLASS_NAME,"_1n_4-zvf0n4aqGEksbgW9N")
for i in range(0,10):
    print(f"Game name {i} -> {game_names[i].text}")


sleep(3)
driver.quit()