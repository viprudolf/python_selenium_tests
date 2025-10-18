from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with (webdriver.Chrome() as driver):
    url = 'https://parsinger.ru/selenium/6/6.3/index.html'
    driver.get(url)
    time.sleep(2)

    text_music = driver.get_cookies()
    m = ''

    for cookie in text_music:
        if 'name' in cookie:
            m = cookie['name']
            break

    phraseInput = driver.find_element(By.ID, 'phraseInput')
    checkButton = driver.find_element(By.ID, 'checkButton')

    phraseInput.send_keys(m)
    checkButton.click()
    time.sleep(5)








