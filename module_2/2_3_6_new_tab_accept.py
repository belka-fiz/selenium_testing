import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from utils import calc

link = "http://suninjuly.github.io/redirect_accept.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    time.sleep(1)

    old_tab = browser.window_handles[0]
    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)

    x_value = float(browser.find_element(By.ID, "input_value").text)
    input_ = browser.find_element(By.CLASS_NAME, "form-control")
    input_.send_keys(calc(x_value))

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    time.sleep(15)
