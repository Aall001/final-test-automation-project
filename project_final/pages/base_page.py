from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://clck.ru/354zU3'
    def go_to_sait(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ES.presence_of_element_located(locator), message=f"Not find {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ES.presence_of_all_elements_located(locator))


#





























