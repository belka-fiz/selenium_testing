import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


with webdriver.Chrome() as browser:
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    WebDriverWait(browser, 12).until(
        ec.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button.click()

    x_value = float(browser.find_element(By.ID, "input_value").text)
    input_ = browser.find_element(By.CLASS_NAME, "form-control")
    input_.send_keys(calc(x_value))

    button = browser.find_element(By.ID, "solve")
    button.click()

    time.sleep(15)
