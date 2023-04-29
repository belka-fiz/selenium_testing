import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

REQUIRED_FIELDS_PLACEHOLDERS = ['first name', 'last name', 'email']
REQUIRED_SELECTORS = [f'div.first_block > * > input[placeholder*="{ph}"]' for ph in REQUIRED_FIELDS_PLACEHOLDERS]
EXPECTED_WELCOME_LINE = "Congratulations! You have successfully registered!"


class TestRegistration(unittest.TestCase):
    def test_registration_1(self):
        with webdriver.Chrome() as browser:
            link = "http://suninjuly.github.io/registration1.html"
            browser.get(link)

            required_fields = [browser.find_element(By.CSS_SELECTOR, selector) for selector in REQUIRED_SELECTORS]
            for field in required_fields:
                field.send_keys("random text")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

            self.assertEqual(welcome_text_elt.text, EXPECTED_WELCOME_LINE)

    def test_registration_2(self):
        with webdriver.Chrome() as browser:
            link = "http://suninjuly.github.io/registration2.html"
            browser.get(link)

            required_fields = [browser.find_element(By.CSS_SELECTOR, selector) for selector in REQUIRED_SELECTORS]
            for field in required_fields:
                field.send_keys("random text")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

            self.assertEqual(welcome_text_elt.text, EXPECTED_WELCOME_LINE)


if __name__ == '__main__':
    unittest.main()
