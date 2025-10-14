import time
from selenium import webdriver

options_chrome = webdriver.ChromeOptions()
# UPDATE в 137 CHROME добавляйте еще строку:
options_chrome.add_argument("--disable-features=DisableLoadExtensionCommandLineSwitch")
options_chrome.add_argument(
    "load-extension=C:\\Users\\rudch\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\ololmadlpnbbagpkjhdomclggmfomhdg\\1.0.0_0"
)
with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://stepik.org/course/104774'
    browser.get(url)
    time.sleep(15)