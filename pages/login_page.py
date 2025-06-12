# login_page.py

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from locators.locators import *
from pages.base_page import BasePage
from helper.url_holder import *

class LoginPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def path(self) -> str:
        return login_url

    @allure.step("Ввод email: {email}")
    def enter_email(self, email: str):
        self.send_keys(LoginPageLocators.EMAIL_FIELD_LOG, email)

    @allure.step("Ввод пароля")
    def enter_password(self, password: str):
        self.send_keys(LoginPageLocators.PASSWORD_FIELD_LOG, password)

    @allure.step("Нажатие на кнопку 'Войти'")
    def submit_login(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Переход на страницу восстановления пароля")
    def go_to_recovery(self):
        self.click(LoginPageLocators.RECOVERY_PASSWORD_LINK)

    def login_user(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.submit_login()
