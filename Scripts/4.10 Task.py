from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC

with (webdriver.Chrome() as driver):
    url = 'https://parsinger.ru/selenium/7/7.html'
    driver.get(url)

    total = 0

    for option in driver.find_elements(By.TAG_NAME, 'option'):
        total += int(option.text)

    input_result = driver.find_element(By.ID, "input_result").send_keys(total)
    btn = driver.find_element(By.CLASS_NAME, "btn").click()
    print(driver.find_element(By.ID, "result").text)
    time.sleep(10)
