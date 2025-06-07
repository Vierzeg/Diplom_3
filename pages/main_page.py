# main_page.py

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from locators.locators import MainPageLocators
from helper.url_holder import *


class MainPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def path(self) -> str:
        return url_base

    @allure.step("Клик по кнопке 'Войти в аккаунт'")
    def click_login_button(self):
        self.click(MainPageLocators.LOGIN_BUTTON)

    @allure.step("Клик по логотипу")
    def click_logo(self):
        self.click(MainPageLocators.LOGO_BUTTON)

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_place_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON)
