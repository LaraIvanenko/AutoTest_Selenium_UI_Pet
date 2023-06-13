import pytest
from pages.profile_page import ProfPage
from pages.data import ProfilePageData
import time

@pytest.mark.regression
def test_delete_pet(browser, go_to_login):
    link = ProfilePageData.PROFILE_URL
    page = ProfPage(browser, link)
    page.open()
    page.go_to_delete_pet()
    time.sleep(5)
    browser.save_screenshot('deletePet.png')

@pytest.mark.smoke
def test_create_pet(browser, go_to_login):
    link = ProfilePageData.PROFILE_URL
    page = ProfPage(browser, link)
    page.open()
    page.go_to_plus_btn()
    time.sleep(2)
    page.go_to_add_name()
    page.go_to_add_type()
    time.sleep(2)
    page.go_to_dog_type()
    page.go_to_add_btn()
    time.sleep(2)
    page.go_to_profile()
    time.sleep(5)
    browser.save_screenshot('createPet.png')
