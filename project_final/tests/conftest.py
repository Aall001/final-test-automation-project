import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome(executable_path=r'../../drivers/chromedriver.exe')
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


