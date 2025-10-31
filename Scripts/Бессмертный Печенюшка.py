import time
from selenium.webdriver.common.by import By
from seleniumwire import webdriver

with webdriver.Chrome() as driver:
    driver.get("https://parsinger.ru/methods/5/index.html")
    time.sleep(2)

    result = 0
    number_link = 0
    max_expiry = 0

    for link in driver.find_elements(By.CLASS_NAME, "urls"):
        link.click()
        get_cookies = driver.get_cookies()
        for c in get_cookies:
            if 'expiry' in c:
                total = int(c['expiry'])
                if max_expiry < total:
                    max_expiry = total

                    result = driver.find_element(By.ID, "result").text

        driver.back()
        number_link = int(link.text)

print(result, number_link)
