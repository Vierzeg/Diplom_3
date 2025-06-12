# conftest.py

import pytest
from utils.browser_factory import BrowserFactory
from utils.api import *
from utils.user_data import *

from pages.main_page import MainPage
from pages.constructor_page import ConstructorPage

# Добавление опции командной строки для выбора браузера
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="Browser: chrome or firefox")

# Фикстура инициализации драйвера (не используется напрямую в тестах)
@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver = BrowserFactory.create_driver(browser_name)
    yield driver
    driver.quit()

# Page Object: MainPage
@pytest.fixture
def main_page(driver):
    return MainPage(driver)

# Page Object: ConstructorPage
@pytest.fixture
def constructor_page(driver):
    return ConstructorPage(driver)

# Фикстура создания и удаления пользователя через API
@pytest.fixture
def create_and_login_user():
    user_data = generate_user()
    response = create_user(user_data)
    response.raise_for_status()
    token = response.json()["accessToken"]
    user_data["accessToken"] = token
    yield user_data
    delete_user(token)


@pytest.fixture
def login_page(driver):
    from pages.login_page import LoginPage
    driver.get(login_url)
    return LoginPage(driver)

@pytest.fixture
def profile_page(driver):
    from pages.profile_page import ProfilePage
    return ProfilePage(driver)

@pytest.fixture
def recovery_page(driver):
    from pages.recovery_page import RecoveryPage
    return RecoveryPage(driver)

@pytest.fixture
def orders_feed_page(driver):
    from pages.orders_feed_page import OrdersFeedPage
    return OrdersFeedPage(driver)