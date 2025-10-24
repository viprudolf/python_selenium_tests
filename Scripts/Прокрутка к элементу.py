import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from seleniumwire import webdriver

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/6/6.5/index.html')

    target = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "target")))

    driver.execute_script("return arguments[0].scrollIntoView(true)", target)

    target.click()
    time.sleep(6)




