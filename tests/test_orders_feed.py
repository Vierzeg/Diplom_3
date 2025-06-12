# test_orders_feed.py
import allure
from locators.locators import *

@allure.feature("Лента заказов")
class TestOrdersFeed:

    @allure.title("Открытие модального окна заказа")
    def test_order_detail_modal(self, login_page, profile_page, orders_feed_page):
        login_page.login_user("pavel18899prac@ya.ru", "Hgr06m_434yf")
        profile_page.go_to_profile()
        profile_page.go_to_order_history()
        orders_feed_page.open_order_detail()

        assert orders_feed_page.is_modal_displayed()

    @allure.title("Проверка счётчиков заказов")
    def test_order_counters(self, orders_feed_page):
        orders_feed_page.open()
        total = orders_feed_page.get_total_orders_count()
        today = orders_feed_page.get_today_orders_count()

        assert total.isdigit() and today.isdigit()
