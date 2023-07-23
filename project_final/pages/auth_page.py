from  project_final.pages.base_page import BasePage
from project_final.pages.locators_page import RostelecomAuthorizationLocators

class AuthNaviBar(BasePage):
    """ Наличие всех элементов на странице Авторизации"""
    def check_navi_bar(self):
        all_list = self.find_elements(RostelecomAuthorizationLocators.LOCATOR_AUTH_NAVI_BAR)
        return [x.text for x in all_list]

class PageRegistr(BasePage):
    """Страница регистрации"""
    def check_page_registr(self):
        page_reg = self.find_elements(RostelecomAuthorizationLocators.LOCATOR_PAGE_REGISTR)
        return [r.text for r in page_reg]
