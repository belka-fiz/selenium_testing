"""
An example for test reruns using pytest-rerunfailures.
The command:
pytest -v --reruns 1 --browser_name=chrome module_3/multi_browser/3_6_8_rerun.py
"""
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")


def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")
