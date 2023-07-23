from project_final.pages.auth_page import AuthNaviBar
from project_final.pages.auth_page import PageRegistr
from project_final.pages.locators_page import AuthoUsers
from selenium.webdriver.common.by import By
from time import sleep



def test_loading_main_page(browser):
    """ EXP-001. Загрузка Авторизационный страницы сайта Ростелеком"""
    main_page = AuthoUsers(browser)
    # Открываем стартовую страницу авторизации
    main_page.go_to_sait()
    assert browser.find_element(By.CLASS_NAME, '.card-container__title').text == 'Авторизация'

def test_all_nav_bar_main_page(browser):
    """EXP-002. Проверяем наличие всех элементов на странице Авторизации, которые указаны в документации."""
    main_page = AuthoUsers(browser)
    main_page.go_to_sait()
    nav_bar_main_page = AuthNaviBar(browser)
    elements = nav_bar_main_page.check_navi_bar()
    assert 'Авторизация' and "Телефон" and "Почта" and "Логин" and "Лицевой счет" in elements
    # Тест не проходит, т.к. наличие элементов на странице не соответсвуют описанию в документации.

def test_auth_input_valid_mail(browser):
    """ EXP-004. Аутентификация пользователя по почте. Ввод валидных значений"""
    main_page = AuthoUsers(browser)
    main_page.go_to_sait()
    main_page.input_username('80ly36zr1enj@mail.ru')
    main_page.input_password('Test12345')
    main_page.button_auth_user()
    assert browser.current_url == 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope=openid&state=faabffcc-8d96-4827-9776-7b1d89281adb&theme=light&auth_type#/'


    """ EXP- 005. Авторизация прошла успешна.После чего мы выполняем выход из аккаунта, обратно на страницу Авторизации"""
    main_page.logout()
    sleep(3)
    assert browser.current_url == 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login?theme%3Dlight&response_type=code&scope=openid&state=a7a55cd3-8bb3-4daa-bf44-61d465272845&theme=light&auth_type'


def test_auth_non_existent_user(browser):
    """ EXP-006. Аутентификация пользователя по почте. Ввод данных не существующего пользователя"""
    main_page = AuthoUsers(browser)
    main_page.go_to_sait()
    main_page.input_username('test@mail.ru')
    main_page.input_password('Test12345')
    main_page.button_auth_user()
    assert browser.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль'

def test_auth_input_invalid_mail(browser):
    """ EXP-007. Аутентификация пользователя по почте. Ввод цифр"""
    main_page = AuthoUsers(browser)
    main_page.go_to_sait()
    main_page.input_username('12345654321')
    main_page.input_password('Test12345')
    main_page.button_auth_user()
    assert browser.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль'

def test_auth_input_invalid_special_characters(browser):
    """ EXP-008. Ввод спец.символов в поле для ввода "Мобильный телефон" """
    main_page = AuthoUsers(browser)
    main_page.go_to_sait()
    main_page.input_mobil_phone('%$##$$@^$#@')
    main_page.input_password('Test12345')
    main_page.button_auth_user()
    assert browser.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль'

def test_auth_input_page_registr(browser):
    """ EXP-009. Переход на страницу регистрации нового пользователя"""
    main_page = AuthoUsers(browser)
    main_page.go_to_sait()
    main_page.input_page_registr()
    nav_bar_page_regiatr = PageRegistr(browser)
    element_registr = nav_bar_page_regiatr.check_page_registr()
    assert 'Регистрация\n' in element_registr

def test_page_user_agreement(browser):
    """ EXP-011. Переход на страницу "Пользовательское соглашение" """
    main_page = AuthoUsers(browser)
    main_page.go_to_sait()
    main_page.page_user_agreement()
    assert browser.find_element(By.TAG_NAME, '//h1').text == "Публичная оферта о заключении Пользовательского соглашения на использование Сервиса «Ростелеком ID»"

def test_page_user_forgot_password(browser):
    """ EXP-012. Переход на страницу "Забыл пароль" """
    main_page = AuthoUsers(browser)
    main_page.go_to_sait()
    main_page.forgot_password()
    assert browser.find_element(By.CLASS_NAME, 'card-container__title').text == 'Восстановление пароля'























