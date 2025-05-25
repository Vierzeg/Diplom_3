# test_recovery.py

import pytest
import allure
from pages.login_page import LoginPage
from pages.recovery_page import RecoveryPage
from locators.locators import *
from helper.url_holder import *
from utils.user_data import generate_user

@allure.feature("Восстановление пароля")
@pytest.mark.usefixtures("driver")
class TestRecoveryPassword:

    @allure.story("Переход на страницу восстановления пароля")
    def test_go_to_recovery_password_page(self, driver):
        driver.get(login_url)
        login = LoginPage(driver)
        login.go_to_recovery()
        login.wait_for_element(RecoveryPageLocators.EMAIL_FIELD)
        assert driver.current_url == res_pass_url

    @allure.story("Ввод почты и отправка формы восстановления")
    def test_recover_password_with_email(self, driver):
        driver.get(res_pass_url)
        recovery = RecoveryPage(driver)
        recovery.enter_email("pavel18899prac@ya.ru")
        recovery.submit_form()
        recovery.wait_for_element(RecoveryPageLocators.CODE_INPUT_FIELD)
        assert driver.current_url == page_res_code_url


    @allure.story("Проверка активации поля при клике на показать/скрыть пароль")
    def test_toggle_password_field_active(self, driver):
        driver.get(login_url)
        recovery = RecoveryPage(driver)
        # Генерируем случайного пользователя
        user = generate_user()
        # Заполняем поля email и пароль
        recovery.set_email(user["email"])
        recovery.set_password(user["password"])
        recovery.wait_for_element(RecoveryPageLocators.SHOW_HIDE_PASSWORD_BUTTON)
        # Нажимаем кнопку показать/скрыть пароль
        recovery.toggle_password_visibility()
        # Проверка, что поле стало типа "text" (пароль виден)
        password_input = recovery.get_element(LoginPageLocators.PASSWORD_FIELD_LOG)
        field_type = password_input.get_attribute("type")
        assert field_type == "text", f"Ожидался тип 'text', но получен '{field_type}'"
