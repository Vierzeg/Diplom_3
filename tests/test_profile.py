# test_profile.py

import pytest
import allure
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from helper.url_holder import login_url
from locators.locators import *

@allure.feature("Личный кабинет")
@pytest.mark.usefixtures("driver")
class TestProfile:

    @allure.story("Переход в личный кабинет")
    def test_go_to_profile(self, driver, create_and_login_user):
        driver.get(login_url)
        login = LoginPage(driver)
        login.login_user(create_and_login_user["email"], create_and_login_user["password"])
        profile = ProfilePage(driver)
        profile.go_to_profile()
        profile.wait_for_element(ProfilePageLocators.PROFILE_LOC)
        assert "account/profile" in driver.current_url

    @allure.story("Переход в раздел История заказов")
    def test_go_to_order_history(self, driver, create_and_login_user):
        driver.get(login_url)
        login = LoginPage(driver)
        login.login_user(create_and_login_user["email"], create_and_login_user["password"])
        profile = ProfilePage(driver)
        profile.go_to_profile()
        profile.go_to_order_history()
        assert "account/order-history" in driver.current_url

    @allure.story("Выход из аккаунта")
    def test_logout(self, driver, create_and_login_user):
        driver.get(login_url)
        login = LoginPage(driver)
        login.login_user(create_and_login_user["email"], create_and_login_user["password"])
        profile = ProfilePage(driver)
        profile.go_to_profile()
        profile.logout()
        profile.wait_for_element(RegisterPageLocators.LOG_IN_ACC_CRIT)
        assert "login" in driver.current_url

