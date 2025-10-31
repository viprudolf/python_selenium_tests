import time
from selenium.webdriver.common.by import By
from seleniumwire import webdriver

with webdriver.Chrome() as driver:
    driver.set_page_load_timeout(5)
    driver.get("https://parsinger.ru/selenium/5.5/3/1.html")

    parents = driver.find_elements(By.CLASS_NAME, 'parent')

    total = 0

    for parent in parents:
        checkbox = parent.find_element(By.CLASS_NAME, 'checkbox')
        textarea = parent.find_element(By.TAG_NAME, 'textarea')
        if checkbox.is_selected():
            num = textarea.get_attribute("value")
            total += int(num)

    print(total)
