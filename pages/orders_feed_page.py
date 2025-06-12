# orders_feed_page.py

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from locators.locators import OrdersFeedPageLocators
from helper.url_holder import *

class OrdersFeedPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def path(self) -> str:
        return feed_url

    @allure.step("Клик по ссылке 'Лента заказов'")
    def click_orders_feed(self):
        self.click(OrdersFeedPageLocators.ORDERS_FEED_LINK)

    @allure.step("Открытие деталей заказа")
    def open_order_detail(self):
        self.click(OrdersFeedPageLocators.ORDER_ITEM)
        self.wait_for_element(OrdersFeedPageLocators.ORDER_DETAIL_MODAL)

    @allure.step("Закрытие модального окна заказа")
    def close_order_detail(self):
        self.click(OrdersFeedPageLocators.CLOSE_MODAL_BUTTON)

    @allure.step("Получение общего количества заказов")
    def get_total_orders_count(self):
        return self.get_text(OrdersFeedPageLocators.TOTAL_ORDERS_COUNTER)

    @allure.step("Получение количества заказов за сегодня")
    def get_today_orders_count(self):
        return self.get_text(OrdersFeedPageLocators.TODAY_ORDERS_COUNTER)

    @allure.step("Получение статуса заказа")
    def get_order_status_text(self):
        return self.get_text(OrdersFeedPageLocators.ORDER_STATUS_TEXT)

    @allure.step("Проверить, отображается ли модальное окно")
    def is_modal_displayed(self):
        return self.is_element_visible(OrdersFeedPageLocators.ORDER_DETAIL_MODAL)