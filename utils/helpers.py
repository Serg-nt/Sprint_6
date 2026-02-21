import requests
import random
import string


def generate_courier_data(length=10):
    """Генерирует случайные данные курьера (логин, пароль и имя)"""
    def generate_random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    return {
        "login": generate_random_string(length),
        "password": generate_random_string(length),
        "first_name": generate_random_string(length)
    }


def register_new_courier_and_return_login_password():

    payload = generate_courier_data()
    response = requests.post(
        'https://qa-scooter.praktikum-services.ru/api/v1/courier',
        data=payload
    )
    return [payload["login"], payload["password"], payload["firstName"]] if response.status_code == 201 else []