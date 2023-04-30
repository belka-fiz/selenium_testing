"""2 types of fixtures with finalizers"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    """A fixture with finalizer after yield"""
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture
def browser_fin(request: pytest.FixtureRequest):
    """A fixture with explicit teardown request.addfinalizer"""
    print("\nstart browser for test..")
    browser = webdriver.Chrome()

    def close_browser():
        browser.quit()

    request.addfinalizer(close_browser)
    return browser


class TestMainPage1:
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser_fin):
        browser_fin.get(link)
        browser_fin.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
