import allure
import pytest
import requests
from ..urls import LOGIN_URL

@allure.feature("Авторизация курьера")
class TestCourierLogin:
    @allure.title("Успешная авторизация")
    def test_successful_login(self, created_courier):
        with allure.step("Подготовка учетных данных"):
            login_data = {
                "login": created_courier["login"],
                "password": created_courier["password"]
            }

        with allure.step("Отправка запроса на авторизацию"):
            response = requests.post(LOGIN_URL, data=login_data)
            allure.attach(str(response.json()), name="Ответ с ID")

        with allure.step("Проверка ответа"):
            assert response.status_code == 200
            assert "id" in response.json()

    @allure.title("Попытка авторизации без поля: {field}")
    @pytest.mark.parametrize("field", ["login", "password"])
    def test_login_required_fields(self, field, created_courier):
        with allure.step("Подготовка данных без обязательного поля"):
            login_data = {
                "login": created_courier["login"],
                "password": created_courier["password"]
            }
            del login_data[field]

        with allure.step("Отправка запроса"):
            response = requests.post(LOGIN_URL, data=login_data)

        with allure.step("Проверка ошибки"):
            assert response.status_code != 200

    @allure.title("Авторизация с неверными учетными данными")
    def test_login_with_wrong_credentials(self):
        with allure.step("Подготовка неверных данных"):
            wrong_credentials = {
                "login": "nonexistent",
                "password": "wrong"
            }

        with allure.step("Отправка запроса"):
            response = requests.post(LOGIN_URL, data=wrong_credentials)

        with allure.step("Проверка ошибки"):
            assert response.status_code == 404