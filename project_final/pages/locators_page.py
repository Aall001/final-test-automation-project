from selenium.webdriver.common.by import By
from project_final.pages.base_page import BasePage


class RostelecomAuthorizationLocators:
    LOCATOR_AUTH_NAVI_BAR = (By.ID, 'page-right')

    LOCATOR_TAB_PHONE = (By.ID, 't-btn-tab-phone')
    LOCATOR_TAB_MAIL = (By.ID, 't-btn-tab-mail')
    LOCATOR_TAB_LOGIN = (By.ID, 't-btn-tab-login')
    LOCATOR_TAB_LS = (By.ID, 't-btn-tab-ls')

    LOCATOR_USERNAME = (By.ID, 'username')
    LOCATOR_PASSWORD = (By.ID, 'password')

    LOCATOR_CHECKBOX_LABEL = (By.XPATH, '//span[@class="rt-checkbox__label"]')
    LOCATOR_FORGOT_PASSWORD = (By.ID, 'forgot_password')

    LOCATOR_BUTTON_INPUT = (By.ID, 'kc-login')
    LOCATOR_USER_AGREEMENT = (By.XPATH, "//a[@class='rt-link rt-link--orange']")

    LOCATOR_REGISTR = (By.ID, 'kc-register')
    LOCATOR_PAGE_REGISTR = (By.ID, 'page-right')

    LOCATOR_BTN_VK = (By.ID, 'oidc_vk')
    LOCATOR_BTN_OK = (By.ID, 'oidc_ok')
    LOCATOR_BTN_MAIL = (By.ID, 'oidc_mail')
    LOCATOR_BTN_YA = (By.ID, 'oidc_ya')

    LOCATOR_LOGOUT = (By.ID, 'logout-btn')



class AuthoUsers(BasePage):
    def input_username(self, name):
        search_username = self.find_element(RostelecomAuthorizationLocators.LOCATOR_USERNAME)
        search_username.click()
        search_username.clear()
        search_username.send_keys(name)
        return search_username

    def input_password(self, password):
        input_pass = self.find_element(RostelecomAuthorizationLocators.LOCATOR_PASSWORD)
        input_pass.click()
        input_pass.clear()
        input_pass.send_keys(password)
        return input_pass

    def button_auth_user(self):
        return self.find_element(RostelecomAuthorizationLocators.LOCATOR_BUTTON_INPUT, time=2).click()

    def logout(self):
        return self.find_element(RostelecomAuthorizationLocators.LOCATOR_LOGOUT, time=2).click()

    def input_mobil_phone(self, numb):
        input_numb = self.find_element(RostelecomAuthorizationLocators.LOCATOR_TAB_PHONE)
        input_numb.click()
        input_numb.clear()
        input_numb.send_keys(numb)
        return input_numb

    def input_page_registr(self):
        return self.find_element(RostelecomAuthorizationLocators.LOCATOR_REGISTR, time=5).click()

    def page_user_agreement(self):
        return self.find_element(RostelecomAuthorizationLocators.LOCATOR_USER_AGREEMENT, time=5).click()

    def forgot_password(self):
        return self.find_element(RostelecomAuthorizationLocators.LOCATOR_FORGOT_PASSWORD, time=5).click()




























