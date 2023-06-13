import time
import pytest
from pages.data import RegisterPageData, RegisterPageDataWrong
from pages.register_page import RegisterPage

@pytest.mark.smoke
def test_go_to_register(browser):
    link = RegisterPageData.REG_PAGE_URL
    page = RegisterPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.go_to_password_conf()
    page.go_to_button()
    time.sleep(5)
    browser.save_screenshot('resultRegister.png')

def test_go_to_register_wrong(browser):
    link = RegisterPageDataWrong.REG_PAGE_URL
    page = RegisterPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password_wrong()
    page.go_to_password_conf_wrong()
    page.go_to_button()
    time.sleep(5)
    browser.save_screenshot('resultRegisterWrong.png')