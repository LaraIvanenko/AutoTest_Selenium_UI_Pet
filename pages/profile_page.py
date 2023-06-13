import time
from selenium.webdriver.common.by import By
from .locators import ProfilePageLocators
from .base_page import BasePage
from pages.data import ProfilePageData
from selenium.webdriver.common.keys import Keys


class ProfPage(BasePage):
    def go_to_delete_pet(self):
        filter_type = self.browser.find_element(*ProfilePageLocators.DEL_BTN)
        filter_type.click()
        time.sleep(1)
        self.browser.find_element(*ProfilePageLocators.YES_BTN).click()

    def go_to_plus_btn(self):
        filter_type = self.browser.find_element(*ProfilePageLocators.ADD_BTN)
        filter_type.click()

    def go_to_add_name(self):
        pet_name = self.browser.find_element(*ProfilePageLocators.NEW_PET_NAME)
        pet_name.send_keys(ProfilePageData.NEW_PET_NAME)

    def go_to_add_type(self):
        pet_type = self.browser.find_element(*ProfilePageLocators.NEW_PET_TYPE)
        pet_type.click()

    def go_to_dog_type(self):
        self.browser.find_element(*ProfilePageLocators.NEW_PET_TYPE_DOG).click()

    def go_to_add_btn(self):
        submit_btn = self.browser.find_element(*ProfilePageLocators.NEW_PET_BTN)
        submit_btn.submit()

    def go_to_profile(self):
        profile_link = self.browser.find_element(*ProfilePageLocators.PROFILE_LINK)
        profile_link.click()
