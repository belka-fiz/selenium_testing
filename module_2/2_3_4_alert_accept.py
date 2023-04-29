import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


with webdriver.Chrome() as browser:
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    time.sleep(1)

    x_value = float(browser.find_element(By.ID, "input_value").text)
    input_ = browser.find_element(By.CLASS_NAME, "form-control")
    input_.send_keys(calc(x_value))

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    time.sleep(15)
