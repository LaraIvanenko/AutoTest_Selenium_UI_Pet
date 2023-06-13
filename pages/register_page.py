from .base_page import BasePage
from .locators import RegPageLocators
from pages.data import RegisterPageData, RegisterPageDataWrong


class RegisterPage(BasePage):
    def go_to_login(self):
        login_email = self.browser.find_element(*RegPageLocators.REG_EMAIL)
        login_email.send_keys(RegisterPageData.REG_EMAIL)

    def go_to_password(self):
        login_pass = self.browser.find_element(*RegPageLocators.REG_PASS)
        login_pass.send_keys(RegisterPageData.REG_PASS)

    def go_to_password_conf(self):
        login_pass = self.browser.find_element(*RegPageLocators.REG_PASS_CONF)
        login_pass.send_keys(RegisterPageData.REG_PASS_CONF)

    def go_to_password_wrong(self):
        login_pass = self.browser.find_element(*RegPageLocators.REG_PASS)
        login_pass.send_keys(RegisterPageDataWrong.REG_PASS)

    def go_to_password_conf_wrong(self):
        login_pass = self.browser.find_element(*RegPageLocators.REG_PASS_CONF)
        login_pass.send_keys(RegisterPageDataWrong.REG_PASS_CONF)

    def go_to_button(self):
        login_btn = self.browser.find_element(*RegPageLocators.REG_BTN)
        login_btn.submit()