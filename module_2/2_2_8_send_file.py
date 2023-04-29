import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
file_name = 'empty.txt'
pwd = os.path.abspath(os.curdir)
file_path = os.path.join(pwd, file_name)

REQUIRED_FIELDS_PLACEHOLDERS = ['first name', 'last name', 'email']
REQUIRED_SELECTORS = [f'div.form-group > input[placeholder*="{ph}"]' for ph in REQUIRED_FIELDS_PLACEHOLDERS]


with webdriver.Chrome() as browser:
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")

    required_fields = [browser.find_element(By.CSS_SELECTOR, selector) for selector in REQUIRED_SELECTORS]

    # Fill the inputs
    for field in required_fields:
        field.send_keys("random text")

    file_input = browser.find_element(By.ID, 'file')
    file_input.send_keys(file_path)

    button.click()
    time.sleep(15)
