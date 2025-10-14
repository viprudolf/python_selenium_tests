import time
from selenium import webdriver

# Задаем опции для Chrome
options_chrome = webdriver.ChromeOptions()
# Указываем путь к профилю пользователя\
options_chrome.add_argument('user-data-dir=C:\\Users\\rudch\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2')

# Инициализируем драйвер с указанными опциями
with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://yandex.ru/'
    browser.get(url)  # Открываем страницу
    time.sleep(10)  # Даем время на загрузку страницы