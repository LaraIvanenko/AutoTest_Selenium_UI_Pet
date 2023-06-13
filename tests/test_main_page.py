import pytest
from pages.main_page import MainPage
from pages.data import MainPageData
import time

@pytest.mark.smoke
def test_go_to_login_page(browser):
    link = MainPageData.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    browser.save_screenshot('resultMainPage.png')

@pytest.mark.smoke
def test_filter_pet_type(browser):
    link = MainPageData.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.go_to_filter_type()
    time.sleep(3)
    browser.save_screenshot('filterByType.png')

@pytest.mark.regression
def test_filter_pet_name(browser):
    link = MainPageData.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.go_to_filter_name()
    time.sleep(1)
    browser.save_screenshot('filterByName.png')

def test_like_without_login(browser):
    link = MainPageData.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.go_to_like_button()
    time.sleep(1)
    browser.save_screenshot('likeWithoutLogin.png')

@pytest.mark.regression
@pytest.mark.xfail
def test_like_with_login(browser, go_to_login):
    link = MainPageData.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.go_to_like_button()
    time.sleep(1)
    browser.save_screenshot('likeWithLogin.png')
