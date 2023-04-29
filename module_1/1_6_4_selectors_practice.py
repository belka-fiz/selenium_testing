import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

find_link = "http://suninjuly.github.io/find_link_text"
form_link = "http://suninjuly.github.io/simple_form_find_task.html"
text = str(math.ceil(math.pow(math.pi, math.e)*10000))

browser = None

try:
    browser = webdriver.Chrome()
    browser.get(find_link)

    link = browser.find_element(By.LINK_TEXT, text)
    link.click()
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
