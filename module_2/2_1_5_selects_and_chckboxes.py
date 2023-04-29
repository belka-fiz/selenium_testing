import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


with webdriver.Chrome() as browser:
    browser.get(link)
    x_element = browser.find_element(By.ID, 'input_value')
    x_value = float(x_element.text)

    y = calc(x_value)

    input_field = browser.find_element(By.ID, 'answer')
    input_field.send_keys(y)

    robobox = browser.find_element(By.ID, 'robotCheckbox')
    robobox.click()

    roboradio = browser.find_element(By.ID, 'robotsRule')
    roboradio.click()

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.submit()

    time.sleep(15)
