# user_data.py

import random
import string


def generate_user():
    email = f"test_{''.join(random.choices(string.ascii_lowercase, k=5))}@yandex.ru"
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    name = ''.join(random.choices(string.ascii_letters, k=8))
    return {
        "email": email,
        "password": password,
        "name": name
    }
