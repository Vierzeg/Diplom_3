# api.py

import requests
import allure
from helper.url_holder import *

@allure.step("Создание пользователя через API")
def create_user(user_data):
    return requests.post(f"{api_url}/auth/register", json=user_data)

@allure.step("Удаление пользователя через API")
def delete_user(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    return requests.delete(f"{api_url}/auth/user", headers=headers)
