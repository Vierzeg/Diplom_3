# constructor_page.py

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.locators import *
from helper.url_holder import *


class ConstructorPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def path(self) -> str:
        return main_url

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_constructor_button(self):
        self.click(ConstructorPageLocators.CONSTRUCTOR_LINK)

    @allure.step("Клик по логотипу для перехода на главную страницу")
    def click_logo(self):
        self.click(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step("Выбор вкладки 'Булки'")
    def select_tab_buns(self):
        self.click(ConstructorPageLocators.BUNS_TAB)

    @allure.step("Выбор вкладки 'Соусы'")
    def select_tab_sauces(self):
        self.click(ConstructorPageLocators.SAUCES_TAB)

    @allure.step("Выбор вкладки 'Начинки'")
    def select_tab_fillings(self):
        self.click(ConstructorPageLocators.FILLINGS_TAB)

    @allure.step("Клик по ингредиенту")
    def click_ingredient(self):
        self.click(ConstructorPageLocators.INGREDIENT)

    # @allure.step("Закрытие модального окна ингредиента")
    # def close_ingredient_modal(self):
    #     self.click(ConstructorPageLocators.INGREDIENT_MODAL_CLOSE)
    @allure.step("Закрытие модального окна ингредиента")
    def close_ingredient_modal(self):
        self.click(ConstructorPageLocators.INGREDIENT_MODAL_CLOSE)
        self.wait.until(EC.invisibility_of_element_located(ConstructorPageLocators.INGREDIENT_MODAL))

    @allure.step("Получение значения счётчика ингредиента")
    def get_ingredient_counter(self) -> str:
        return self.get_text(ConstructorPageLocators.INGREDIENT_COUNTER)

    @allure.step("Ожидание отображения модального окна ингредиента")
    def wait_for_ingredient_modal(self):
        self.wait_for_element(ConstructorPageLocators.INGREDIENT_MODAL)

    @allure.step("Добавление ингредиента в корзину")
    def add_ingredient_to_cart(self):
        ingredient = self.find_element(ConstructorPageLocators.INGREDIENT)
        drop_zone = self.find_element(ConstructorPageLocators.CART_DROPZONE)
        actions = ActionChains(self.driver)
        actions.click_and_hold(ingredient).pause(0.5).move_to_element(drop_zone).pause(0.5).release().perform()

    @allure.step("Проверка, что модальное окно отображается")
    def is_modal_ingr_displayed(self) -> bool:
        return self.is_element_visible(ConstructorPageLocators.INGREDIENT_MODAL)

    @allure.step("Проверка, что модальное окно ингредиента закрыто")
    def is_close_modal_ingr(self) -> bool:
        return not self.is_element_visible(ConstructorPageLocators.INGREDIENT_MODAL)
