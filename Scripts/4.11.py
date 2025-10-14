from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC

with (webdriver.Chrome() as driver):
    url = 'https://parsinger.ru/selenium/6/6.html'
    driver.get(url)

    value = ((12434107696 * 3) * 2) + 1

    for option in driver.find_elements(By.TAG_NAME, "option"):
        value = int(option.text)
        if value == value:
            option.click()

    time.sleep(2)
    btn_box = driver.find_element(By.CLASS_NAME, "btn_box").click()
    print(driver.find_element(By.ID, "result").text)
    time.sleep(2)
