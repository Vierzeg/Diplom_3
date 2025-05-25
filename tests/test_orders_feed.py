# test_orders_feed.py

import pytest
import allure
from pages.login_page import LoginPage
from pages.orders_feed_page import OrdersFeedPage
from pages.profile_page import ProfilePage
from helper.url_holder import *
from locators.locators import *

@allure.feature("Лента заказов")
@pytest.mark.usefixtures("driver")
class TestOrdersFeed:

    @allure.story("Открытие модального окна заказа")
    def test_order_detail_modal(self, driver):
        driver.get(login_url)
        login = LoginPage(driver)
        login.login_user("pavel18899prac@ya.ru", "Hgr06m_434yf")
        profile = ProfilePage(driver)
        profile.go_to_profile()
        profile.wait_for_element(ProfilePageLocators.PROFILE_LOC)
        profile.go_to_order_history()
        feed = OrdersFeedPage(driver)
        feed.open_order_detail()
        feed.wait_for_element(OrdersFeedPageLocators.ORDER_DETAIL_MODAL)
        assert feed.is_modal_displayed()

    @allure.story("Проверка счётчиков заказов")
    def test_order_counters(self, driver):
        driver.get(feed_url)
        feed = OrdersFeedPage(driver)
        total = feed.get_total_orders_count()
        today = feed.get_today_orders_count()
        assert total.isdigit() and today.isdigit()
