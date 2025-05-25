# register_page.py

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from locators.locators import RegisterPageLocators

class RegisterPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("Ввод имени: {name}")
    def enter_name(self, name: str):
        self.send_keys(RegisterPageLocators.NAME_FIELD, name)

    @allure.step("Ввод email: {email}")
    def enter_email(self, email: str):
        self.send_keys(RegisterPageLocators.EMAIL_FIELD, email)

    @allure.step("Ввод пароля")
    def enter_password(self, password: str):
        self.send_keys(RegisterPageLocators.PASSWORD_FIELD, password)

    @allure.step("Клик по кнопке 'Зарегистрироваться'")
    def click_register(self):
        self.click(RegisterPageLocators.REGISTER_BUTTON)

    @allure.step("Получение текста ошибки о некорректном пароле")
    def get_incorrect_password_error(self):
        return self.get_text(RegisterPageLocators.INCORRECT_PASSWORD_ERROR)
