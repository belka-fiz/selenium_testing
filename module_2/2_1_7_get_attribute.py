import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from utils import calc

link = "http://suninjuly.github.io/get_attribute.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    treasure = browser.find_element(By.ID, 'treasure')
    x_value = float(treasure.get_attribute('valuex'))

    y = calc(x_value)

    input_field = browser.find_element(By.ID, 'answer')
    input_field.send_keys(y)

    robobox = browser.find_element(By.ID, 'robotCheckbox')
    robobox.click()

    roboradio = browser.find_element(By.ID, 'robotsRule')
    roboradio.click()

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.submit()

    time.sleep(30)
