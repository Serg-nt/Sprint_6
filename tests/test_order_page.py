import allure
import pytest
from ..page_objects.main_page import MainPage
from ..page_objects.order_page import OrderPage
from ..data.order_page_data import order_test_data
from ..urls import MAIN_PAGE_URL


@allure.feature("Оформление заказа")
@pytest.mark.usefixtures("driver")
class TestOrderPage:

    @pytest.mark.parametrize(
        "name,surname,address,phone,metro_station,date,rent_period,comment", 
        order_test_data
    )
    @allure.story("Позитивный сценарий оформления заказа")
    @allure.title("Оформление заказа для {name} {surname}")
    def test_order_creation(self, name, surname, address, phone, metro_station, date, rent_period, comment):
        main_page = MainPage(self.driver)
        order_page = OrderPage(self.driver)
        
        with allure.step("Открыть главную страницу"):
            main_page.open()

        with allure.step("Начать оформление заказа"):
            main_page.click_order_header_button()
            order_page.is_for_rent_header_visible()

        with allure.step("Заполнить данные пользователя"):
            order_page.fill_name(name)
            order_page.fill_surname(surname)
            order_page.fill_address(address)
            order_page.fill_phone(phone)
            order_page.select_metro_station(metro_station)
            order_page.click_next_button()

        with allure.step("Заполнить данные аренды"):
            order_page.select_date(date)
            order_page.select_rent_period(rent_period)
            order_page.select_black_color()
            order_page.fill_comment(comment)

        with allure.step("Подтвердить заказ"):
            order_page.click_order_button()
            order_page.confirm_order()

        with allure.step("Проверить номер заказа"):
            order_number_text = order_page.get_order_number_text()
            assert "Номер заказа" in order_number_text

    @allure.story("Переход по логотипу Самокат")
    @allure.title("Проверка перехода по логотипу Самокат")
    def test_logo_samokat(self):
        main_page = MainPage(self.driver)
        order_page = OrderPage(self.driver)
        
        with allure.step("Открыть главную страницу"):
            main_page.open()

        with allure.step("Начать оформление заказа"):
            main_page.click_order_bottom_button()
            order_page.is_for_rent_header_visible()

        with allure.step("Вернуться на главную через логотип"):
            order_page.click_samokat_logo()

        with allure.step("Проверить URL главной страницы"):
            assert main_page.is_current_url_matches(MAIN_PAGE_URL)
