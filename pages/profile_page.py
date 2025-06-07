# profile_page.py

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from locators.locators import ProfilePageLocators
from helper.url_holder import *


class ProfilePage(BasePage):

    @property
    def path(self):
        return login_url

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        """Переопределяем open, чтобы избежать ошибки 'str' object is not callable"""
        self.driver.get(self.path)

    @allure.step("Клик по кнопке 'Личный кабинет'")
    def go_to_profile(self):
        self.click(ProfilePageLocators.PROFILE_BUTTON)
        self.wait_for_element(ProfilePageLocators.PROFILE_LOC)


    @allure.step("Клик по кнопке 'История заказов'")
    def go_to_order_history(self):
        self.click(ProfilePageLocators.ORDER_HISTORY_BUTTON)

    @allure.step("Клик по кнопке 'Выход'")
    def logout(self):
        self.click(ProfilePageLocators.LOGOUT_BUTTON)
