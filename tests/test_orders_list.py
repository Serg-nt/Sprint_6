import allure
import pytest
import requests
from ..urls import ORDERS_URL

@allure.feature("Список заказов")
class TestOrdersList:
    @allure.title("Получение списка заказов")
    def test_get_orders_list(self):
        with allure.step("Отправка запроса на получение списка"):
            response = requests.get(ORDERS_URL)
            allure.attach(str(response.json()), name="Список заказов")

        with allure.step("Проверка ответа"):
            assert response.status_code == 200
            assert "orders" in response.json()
            assert isinstance(response.json()["orders"], list)