# test_recovery.py

import pytest
import allure
from locators.locators import *
from helper.url_holder import *
from utils.user_data import generate_user

@allure.feature("Восстановление пароля")
@pytest.mark.usefixtures("driver")
class TestRecoveryPassword:

    @allure.title("Переход на страницу восстановления пароля")
    def test_go_to_recovery_password_page(self, login_page, recovery_page):
        login_page.open()  # открываем страницу логина
        login_page.go_to_recovery()
        recovery_page.wait_for_element(RecoveryPageLocators.EMAIL_FIELD)
        assert recovery_page.driver.current_url == res_pass_url

    @allure.title("Ввод почты и отправка формы восстановления")
    def test_recover_password_with_email(self, recovery_page):
        recovery_page.open()  # открываем страницу восстановления пароля
        recovery_page.enter_email("pavel18899prac@ya.ru")
        recovery_page.submit_form()
        recovery_page.wait_for_element(RecoveryPageLocators.CODE_INPUT_FIELD)
        assert recovery_page.driver.current_url == page_res_code_url

    @allure.title("Проверка активации поля при клике на показать/скрыть пароль")
    def test_toggle_password_field_active(self, recovery_page):
        recovery_page.open(login_url)
        user = generate_user()  # Вызов функции прямо здесь
        recovery_page.set_email(user["email"])
        recovery_page.set_password(user["password"])
        recovery_page.wait_for_element(RecoveryPageLocators.SHOW_HIDE_PASSWORD_BUTTON)
        recovery_page.toggle_password_visibility()
        password_input = recovery_page.find_element(LoginPageLocators.PASSWORD_FIELD_LOG)
        field_type = password_input.get_attribute("type")
        assert field_type == "text", f"Ожидался тип 'text', но получен '{field_type}'"
