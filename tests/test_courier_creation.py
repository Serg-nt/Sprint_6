import pytest
import allure
import requests

from ..urls import COURIER_URL, LOGIN_URL, API_URL
from ..utils.helpers import generate_courier_data

class TestCourierCreation:
    @allure.title("Успешное создание курьера")
    @allure.description("Проверка что курьер может быть успешно создан")
    def test_successful_creation(self):
        with allure.step("Подготовка тестовых данных"):
            courier_data = generate_courier_data()
            
        with allure.step("Создание курьера"):
            response = requests.post(COURIER_URL, data=courier_data)
            
        with allure.step("Проверка ответа"):
            allure.attach(str(response.status_code), name="Status Code")
            allure.attach(str(response.json()), name="Response Body")
            assert response.status_code == 201
            assert response.json() == {"ok": True}
            
        with allure.step("Удаление тестовых данных"):
            self._delete_courier(courier_data)

    @allure.title("Попытка создания дубликата курьера")
    def test_duplicate_creation_fails(self):
        with allure.step("Подготовка данных"):
            courier_data = generate_courier_data()
        
        with allure.step("Первое успешное создание"):
            create_response = requests.post(COURIER_URL, data=courier_data)
            assert create_response.status_code == 201

        with allure.step("Попытка создания дубликата"):
            duplicate_response = requests.post(COURIER_URL, data=courier_data)
            allure.attach(str(duplicate_response.json()), name="Ошибка дубликата")
            assert duplicate_response.status_code == 409

        with allure.step("Очистка данных"):
            self._delete_courier(courier_data)

    @allure.title("Проверка обязательных полей: {missing_field}")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_required_fields(self, missing_field):
        with allure.step("Подготовка данных без обязательного поля"):
            courier_data = generate_courier_data()
            del courier_data[missing_field]
            allure.attach(str(courier_data), name="Данные без поля")

        with allure.step("Отправка запроса"):
            response = requests.post(COURIER_URL, data=courier_data)
            assert response.status_code == 400

        if "login" in courier_data and "password" in courier_data:
            with allure.step("Очистка данных"):
                self._delete_courier(courier_data)

    def _delete_courier(self, courier_data):
        with allure.step("Авторизация для получения ID"):
            login_response = requests.post(LOGIN_URL, data={
                "login": courier_data["login"],
                "password": courier_data["password"]
            })
        
        if login_response.status_code == 200:
            with allure.step("Удаление курьера"):
                courier_id = login_response.json().get("id")
                requests.delete(f"{COURIER_URL}/{courier_id}")