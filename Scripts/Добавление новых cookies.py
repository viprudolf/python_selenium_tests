from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with (webdriver.Chrome() as driver):
    url = 'https://parsinger.ru/selenium/6/6.3.3/index.html'
    driver.get(url)
    time.sleep(2)

    pprint(driver.get_cookies())

    driver.add_cookie({"name":'secretKey', "value":'selenium123'})

    driver.refresh()
    time.sleep(2)

    driver.get_cookies()

    password = driver.find_element(By.ID, "password").text
    print(password)
    time.sleep(6)











