from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC



with webdriver.Chrome() as driver:

    url = "https://parsinger.ru/selenium/2/2.html"

    driver.get(url)
    time.sleep(2)

    title_text = driver.find_elements(By.PARTIAL_LINK_TEXT, "16243162441624")
    for links in title_text:
        links.click()

    result = driver.find_element(By.ID, "result")
    time.sleep(2)

    print(result.text)

    time.sleep(10)




