# test_profile.py

import allure
from locators.locators import *

@allure.feature("Личный кабинет")
class TestProfile:

    @allure.title("Переход в личный кабинет")
    def test_go_to_profile(self, login_page, profile_page, create_and_login_user):
        login_page.login_user(create_and_login_user["email"], create_and_login_user["password"])
        profile_page.go_to_profile()
        profile_page.wait_for_element(ProfilePageLocators.PROFILE_LOC)
        assert "account/profile" in profile_page.driver.current_url

    @allure.title("Переход в раздел История заказов")
    def test_go_to_order_history(self, login_page, profile_page, create_and_login_user):
        login_page.login_user(create_and_login_user["email"], create_and_login_user["password"])
        profile_page.go_to_profile()
        profile_page.go_to_order_history()
        assert "account/order-history" in profile_page.driver.current_url

    @allure.title("Выход из аккаунта")
    def test_logout(self, login_page, profile_page, create_and_login_user):
        login_page.login_user(create_and_login_user["email"], create_and_login_user["password"])
        profile_page.go_to_profile()
        profile_page.logout()
        profile_page.wait_for_element(RegisterPageLocators.LOG_IN_ACC_CRIT)
        assert "login" in profile_page.driver.current_url
