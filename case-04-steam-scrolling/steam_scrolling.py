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
wait = WebDriverWait(driver, 5)

page_url = "https://store.steampowered.com/charts/topselling/NL"
driver.get(page_url)
driver.maximize_window()
accept_cookies(driver, wait)

# Scroll to bottom
driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
sleep(3)

# Scroll back to top
driver.execute_script("window.scrollTo(document.documentElement.scrollHeight,0);")

# Scroll to specific element
element = driver.find_element(By.XPATH, '//*[@id="page_root"]/div/div/div/div[2]/div/div/div[3]/table/tbody/tr[40]')
driver.execute_script("arguments[0].scrollIntoView();", element)
driver.execute_script("window.scrollBy(0,800)")

# Keyboard navigation - go to end and back to start
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
sleep(3)
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)

sleep(3)
driver.quit()