import time

from selenium.webdriver.common.by import By
from seleniumwire import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as driver:
    driver.set_page_load_timeout(5)
    driver.get("https://parsinger.ru/scroll/4/index.html")
    time.sleep(2)

    btn = driver.find_elements(By.CLASS_NAME, "btn")

    number_in_result = 0

    for element_btn in btn:
        driver.execute_script("return arguments[0].scrollIntoView(true);", element_btn)
        if element_btn.is_displayed() and element_btn.is_enabled():
            element_btn.click()
            result = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.ID, "result"))
            )
            if result.is_displayed() and result.is_enabled():
                number_in_result += int(result.text)

print(number_in_result)
