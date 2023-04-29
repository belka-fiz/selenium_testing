import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


link = "http://suninjuly.github.io/execute_script.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    x = float(browser.find_element(By.ID, 'input_value').text)
    answer = calc(x)

    robobox = browser.find_element(By.ID, 'robotCheckbox')
    robobox.click()

    answer_inpt = browser.find_element(By.ID, 'answer')
    answer_inpt.send_keys(str(answer))

    button = browser.find_element(By.CLASS_NAME, 'btn')
    script = "return arguments[0].scrollIntoView(true);"
    browser.execute_script(script, button)

    roboradio = browser.find_element(By.ID, 'robotsRule')
    roboradio.click()
    button.click()

    time.sleep(20)
