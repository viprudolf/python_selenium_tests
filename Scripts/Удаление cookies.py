from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with (webdriver.Chrome() as driver):
    url = 'https://parsinger.ru/selenium/6/6.3.2/index.html'
    driver.get(url)
    time.sleep(2)

    pprint(driver.get_cookies())

    if driver.get_cookies():
        driver.delete_all_cookies()

    pprint(driver.get_cookies())
    time.sleep(6)











