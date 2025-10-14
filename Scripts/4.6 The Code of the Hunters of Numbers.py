from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC



with (webdriver.Chrome() as driver):

    url = "https://parsinger.ru/selenium/3/3.html"
    driver.get(url)

    total_value = 0

    class_text = driver.find_elements(By.XPATH, "//p[2]")

    for values in class_text:
        total_value += int(values.text)

    print(total_value)

    time.sleep(10)

