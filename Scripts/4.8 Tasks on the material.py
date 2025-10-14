from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC



with (webdriver.Chrome() as driver):

    url = 'https://parsinger.ru/selenium/4/4.html'
    driver.get(url)

    btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn"))
    )
    btn.click()

    checked = driver.find_elements(By.CLASS_NAME, "check")
    result = driver.find_element(By.ID, "result")

    for i in checked:
        i.click()
        print("Нажал")
        time.sleep(2)

    time.sleep(3)

    print(result.text)

