import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    select = Select(browser.find_element(By.ID, 'dropdown'))

    num1 = int(browser.find_element(By.ID, 'num1').text)
    num2 = int(browser.find_element(By.ID, 'num2').text)
    answer = num1 + num2

    select.select_by_value(str(answer))

    submit = browser.find_element(By.CLASS_NAME, 'btn')
    submit.submit()

    time.sleep(30)
