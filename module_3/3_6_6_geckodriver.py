"""First run of Firefox browser"""

import time

from selenium import webdriver

with webdriver.Firefox() as driver:
    driver.get("https://stepik.org/lesson/25969/step/8")
    time.sleep(20)
