# test_main_functionality.py

import allure

@allure.epic("Основной функционал конструктора")
class TestMainFunctionality:

    @allure.title("Переход по клику на логотип к 'Конструктору'")
    def test_go_to_constructor(self, main_page, constructor_page):
        main_page.open()
        main_page.click_logo()
        assert constructor_page.is_opened()

    @allure.title("Клик по ингредиенту — открытие и закрытие модального окна")
    def test_ingredient_modal_open_close(self, constructor_page):
        constructor_page.open()
        constructor_page.click_ingredient()
        constructor_page.wait_for_ingredient_modal()
        assert constructor_page.is_modal_ingr_displayed()

        constructor_page.close_ingredient_modal()
        assert constructor_page.is_close_modal_ingr()

    @allure.title("Добавление ингредиента увеличивает счётчик")
    def test_ingredient_counter_increases(self, constructor_page):
        constructor_page.open()
        initial_count = constructor_page.get_ingredient_counter()

        constructor_page.add_ingredient_to_cart()

        updated_count = constructor_page.get_ingredient_counter()
        assert int(updated_count) > int(initial_count)
