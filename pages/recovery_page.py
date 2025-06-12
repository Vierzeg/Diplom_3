# recovery_page.py

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from locators.locators import *
from helper.url_holder import *
class RecoveryPage(BasePage):


    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def path(self) -> str:
        return res_pass_url


    @allure.step("Ввод email для восстановления: {email}")
    def enter_email(self, email: str):
        self.send_keys(RecoveryPageLocators.EMAIL_FIELD, email)

    @allure.step("Отправка формы восстановления пароля")
    def submit_form(self):
        self.click(RecoveryPageLocators.SUBMIT_BUTTON)

    @allure.step("Показать/скрыть пароль")
    def toggle_password_visibility(self):
        self.click(RecoveryPageLocators.SHOW_HIDE_PASSWORD_BUTTON)

    def set_email(self, email):
        self.send_keys(LoginPageLocators.EMAIL_FIELD_LOG, email)

    def set_password(self, password):
        self.send_keys(LoginPageLocators.PASSWORD_FIELD_LOG, password)
