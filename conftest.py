import pytest
from selenium import webdriver
from pages.data import LoginPageData
from pages.login_page import LoginPage

@pytest.fixture(autouse=True)
# @pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.fixture()
def go_to_login(browser):
    link = LoginPageData.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.go_to_button()