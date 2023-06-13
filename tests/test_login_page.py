import time
from pages.data import LoginPageData, LoginPageDataWrong
from pages.login_page import LoginPage
import pytest


@pytest.mark.smoke
def test_go_to_login(browser):
    link = LoginPageData.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.go_to_button()
    time.sleep(5)
    browser.save_screenshot('resultLogin.png')

def test_go_to_login_wrong(browser):
    link = LoginPageDataWrong.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_wrong()
    page.go_to_password_wrong()
    page.go_to_button()
    time.sleep(5)
    browser.save_screenshot('resultLoginWrong.png')

