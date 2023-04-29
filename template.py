import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/execute_script.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    time.sleep(15)
