# conftest.py

import pytest
from utils.browser_factory import *
from utils.api import *
from utils.user_data import *
from helper.url_holder import *

# Добавление опции командной строки для выбора браузера
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="Browser: chrome or firefox")

# Фикстура инициализации браузера
@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver = BrowserFactory.create_driver(browser_name)
    driver.get(main_url)
    yield driver
    driver.quit()

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