"""
Exercise for using parametrization. In this case - using a list variable
Requires additional file 'confidential.py' with cookies dict for logged-in user at stepik.org in the following format
cookies = [{'name': 'csrftoken', 'value': 'your_csrftoken_value'},
           {'name': 'sessionid', 'value': 'your_sessionid_value'}]
"""

import math
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from confidential import cookies


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


links = ["https://stepik.org/lesson/236895/step/1",
         "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1",
         "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1",
         "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1",
         "https://stepik.org/lesson/236905/step/1"]


@pytest.mark.parametrize('link', links)
def test_login(browser, link):
    browser.get(link)
    for cookie in cookies:
        browser.add_cookie(cookie)
    browser.refresh()

    WebDriverWait(browser, 20).until(ec.presence_of_element_located(
        (By.CSS_SELECTOR, "textarea.string-quiz__textarea")))
    answer_input = browser.find_element(By.CSS_SELECTOR, "textarea.string-quiz__textarea")
    answer = math.log(int(time.time()))
    answer_input.send_keys(answer)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
    submit_button.click()

    WebDriverWait(browser, 30).until(ec.presence_of_element_located(
        (By.CSS_SELECTOR, ".smart-hints__hint")
    ))
    feedback_area = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
    assert feedback_area.text == "Correct!"
