# test_main_functionality.py

import pytest
import allure
from pages.main_page import MainPage
from pages.constructor_page import ConstructorPage
from helper.url_holder import main_url

@allure.feature("Основной функционал")
@pytest.mark.usefixtures("driver")
class TestMainFunctionality:

    @allure.story("Переход на Конструктор")
    def test_go_to_constructor(self, driver):
        main = MainPage(driver)
        driver.get(main_url)
        main.click_logo()
        constructor = ConstructorPage(driver)
        constructor.click_constructor_button()
        assert driver.current_url == main_url or "/constructor" in driver.current_url

    @allure.story("Клик по ингредиенту — открытие и закрытие модалки")
    def test_ingredient_modal_open_close(self, driver):
        driver.get(main_url)
        constructor = ConstructorPage(driver)
        constructor.click_ingredient()
        assert constructor.is_modal_ingr_displayed()
        constructor.close_ingredient_modal()
        assert constructor.is_close_modal_ingr()

    @allure.story("Добавление ингредиента увеличивает счётчик")
    def test_ingredient_counter_increases(self, driver):
        driver.get(main_url)
        constructor = ConstructorPage(driver)
        initial_count = int(constructor.get_ingredient_counter())
        constructor.add_ingredient_to_cart()
        updated_count = int(constructor.get_ingredient_counter())
        assert updated_count == initial_count + 2
