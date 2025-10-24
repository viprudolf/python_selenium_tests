import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from seleniumwire import webdriver

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.5/1/1.html')

    for text in driver.find_elements(By.CLASS_NAME, "text-field"):
        text.clear()
        checkButton = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID, "checkButton")))
        checkButton.click()

    print(driver.switch_to.alert.text)
    time.sleep(5)

