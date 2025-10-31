from seleniumwire import webdriver

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/methods/3/index.html')

    get_cookies = driver.get_cookies()

    value = 0

    for cookie in get_cookies:
        name = cookie['name']
        print(name)
        if "_" in name:
            param = int(name.split("_")[-1])
            if param % 2 == 0:
                name_value = int(cookie['value'])
                value += name_value
print(f"Сумма {value}")
