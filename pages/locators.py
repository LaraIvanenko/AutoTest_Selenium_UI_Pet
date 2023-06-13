from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    FIRST_LIKE = (By.CSS_SELECTOR, '.col-12:nth-child(4) .product-grid-item-bottom .pi')
    PET_NAME = (By.ID, "petName")
    PET_TYPE = (By.ID, "typesSelector")

class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")

class RegPageLocators:
    REG_EMAIL = (By.ID, "login")
    REG_PASS = (By.CSS_SELECTOR, "#password > .p-inputtext")
    REG_PASS_CONF = (By.CSS_SELECTOR, "#confirm_password > .p-inputtext")
    REG_BTN = (By.CSS_SELECTOR, ".p-button-label")

class ProfilePageLocators:
    ADD_BTN = (By.CSS_SELECTOR, ".pi-plus")
    DEL_BTN = (By.CSS_SELECTOR, ".col-12:nth-child(1) .p-button-danger")
    YES_BTN = (By.CSS_SELECTOR, ".p-confirm-popup-accept > .p-button-label")
    NEW_PET_NAME = (By.ID, "name")
    NEW_PET_TYPE = (By.CSS_SELECTOR, '#typeSelector')
    NEW_PET_BTN = (By.CSS_SELECTOR, ".p-button-success > .p-button-label")
    PROFILE_LINK = (By.CSS_SELECTOR, ".p-menuitem:nth-child(1) .p-menuitem-text")
    NEW_PET_TYPE_DOG = (By.XPATH, '//*[@aria-label="dog"]')
