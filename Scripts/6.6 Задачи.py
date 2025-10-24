import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from seleniumwire import webdriver

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/methods/1/index.html')

    while True:
        result = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "result")))
        numbers = result.text

        if numbers.isdigit():
            print(numbers)
            break
        else:
            driver.refresh()

