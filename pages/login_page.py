from .base_page import BasePage
from .locators import LoginPageLocators
from pages.data import LoginPageData, LoginPageDataWrong


class LoginPage(BasePage):
    def go_to_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(LoginPageData.LOGIN_EMAIL)

    def go_to_password(self):
        login_pass = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_pass.send_keys(LoginPageData.LOGIN_PASS)

    def go_to_button(self):
        login_btn = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_btn.submit()

    def go_to_login_wrong(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(LoginPageDataWrong.LOGIN_EMAIL)

    def go_to_password_wrong(self):
        login_pass = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_pass.send_keys(LoginPageDataWrong.LOGIN_PASS)


