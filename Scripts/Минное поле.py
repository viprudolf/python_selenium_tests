from selenium.webdriver.common.by import By
from seleniumwire import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as driver:
    driver.get("https://parsinger.ru/selenium/5.5/2/1.html")

    text_fields = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "text-field"))
    )

    for text in text_fields:
        if text.get_attribute("disabled") is None:
            text.clear()

    checkButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "checkButton"))).click()

    print(driver.switch_to.alert.text)



