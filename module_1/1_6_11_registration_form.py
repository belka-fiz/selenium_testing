"""
Test exercise for students review.
A bit overcommented about obvious things for education purposes
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Generating selectors list.
REQUIRED_FIELDS_PLACEHOLDERS = ['first name', 'last name', 'email']
REQUIRED_SELECTORS = [f'div.first_block > * > input[placeholder*="{ph}"]' for ph in REQUIRED_FIELDS_PLACEHOLDERS]
# The placeholders on the page under test may be changed, so it's a good practice to
# have them separated from the code to be able to modify them easily

with webdriver.Chrome() as browser:
    # Visit the registration page
    link = "http://suninjuly.github.io/registration2.html"
    browser.get(link)

    # Find the required input elements
    required_fields = [browser.find_element(By.CSS_SELECTOR, selector) for selector in REQUIRED_SELECTORS]

    # Fill the inputs
    for field in required_fields:
        field.send_keys("random text")
        # of course, in real tests we should fill each input separately according to its validation rules,
        # but in this exercise we practice other subject.

    # Sending the form
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Registration success check

    # waiting for the page to load
    time.sleep(1)  # please, update the field if it fails to load in 1 second

    # Finding the element
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

    # Verifying the text
    assert welcome_text_elt.text == "Congratulations! You have successfully registered!"  # noqa

    time.sleep(10)

# I prefer using context manager instead of try/finally. It is simpler, and a bit prettier.
# Selenium allows you to do it without reinventing the wheel, see
# https://stackoverflow.com/a/54149666 and https://github.com/SeleniumHQ/selenium/pull/5919
