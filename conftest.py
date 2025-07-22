import pytest
import requests
from .urls import COURIER_URL, LOGIN_URL
from .utils.helpers import generate_courier_data

@pytest.fixture
def created_courier():
    """Фикстура создания и удаления тестового курьера"""
    courier_data = generate_courier_data()
    response = requests.post(COURIER_URL, data=courier_data)
    yield courier_data
    
    # Удаление после теста
    login_data = {
        "login": courier_data["login"],
        "password": courier_data["password"]
    }
    login_response = requests.post(LOGIN_URL, data=login_data)
    if login_response.status_code == 200:
        courier_id = login_response.json()["id"]
        requests.delete(f"{COURIER_URL}/{courier_id}")