import time
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .base_page import BasePage
from pages.data import MainPageData
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_filter_type(self):
        filter_type = self.browser.find_element(*MainPageLocators.PET_TYPE)
        filter_type.click()
        time.sleep(1)
        self.browser.find_element(By.ID, MainPageData.PET_TYPE_FILTER).click()

    def go_to_filter_name(self):
        filter_type = self.browser.find_element(*MainPageLocators.PET_NAME)
        filter_type.send_keys(MainPageData.PET_NAME_FILTER)
        filter_type.send_keys(Keys.ENTER)

    def go_to_like_button(self):
        like_btn = self.browser.find_element(*MainPageLocators.FIRST_LIKE)
        like_btn.click()