import allure
import pytest
import requests
from ..urls import ORDERS_URL

@allure.feature("Создание заказа")
class TestOrderCreation:
    @allure.title("Создание заказа с цветами: {color}")
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ], ids=["BLACK", "GREY", "BLACK_GREY", "NO_COLOR"])
    def test_create_order_with_colors(self, color):
        with allure.step("Подготовка данных заказа"):
            order_data = {
                "firstName": "Тест",
                "lastName": "Тестов",
                "address": "Москва",
                "metroStation": "1",
                "phone": "+79999999999",
                "rentTime": 1,
                "deliveryDate": "2025-07-30",
                "comment": "Тест",
                "color": color
            }
            allure.attach(str(order_data), name="Данные заказа")

        with allure.step("Отправка запроса"):
            response = requests.post(ORDERS_URL, json=order_data)
            allure.attach(str(response.json()), name="Ответ")

        with allure.step("Проверка ответа"):
            assert response.status_code == 201
            assert "track" in response.json()