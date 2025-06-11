from selenium import webdriver
import pytest
import allure

from ..page_objects.main_page import MainPage
from ..page_objects.order_page import OrderPage


@allure.feature("Оформление заказа")
class TestOrderPage:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize("name,surname,address,phone,metro_station,date,rent_period,color,comment", [
        ("Алекс", "Пехов", "Москва", "79000000000", "Черкизовская", 15, "трое суток", "black", "Комментарий 2"),
        ("Ирина", "Иванова", "Санкт-Петербург", "79111234567", "Парк Победы", 20, "двое суток", "black", "Комментарий тест3"),
    ])
    @allure.story("Позитивный сценарий оформления заказа")
    @allure.title("Тест оформления заказа: {name} {surname}, {metro_station}, {date} число")
    def test_order(self, name, surname, address, phone, metro_station, date, rent_period, color, comment):
        with allure.step("Открыть главную страницу"):
            self.driver.get('https://qa-scooter.praktikum-services.ru/')

        main_page = MainPage(self.driver)
        order_page = OrderPage(self.driver)

        with allure.step("Перейти к форме заказа"):
            main_page.scroll_to_header_button()
            main_page.click_order_header_button()
            order_page.check_header_for_rent()

        with allure.step("Заполнить форму пользователя"):
            order_page.fill_name(name)
            order_page.fill_surname(surname)
            order_page.fill_address(address)
            order_page.fill_phone(phone)
            order_page.select_metro_option_by_name(metro_station)
            order_page.click_next_is_enabled()

        with allure.step("Заполнить данные аренды"):
            order_page.check_header_about_rent()
            order_page.select_date(day=date)
            order_page.select_rent_period(option_text=rent_period)
            if color == "black":
                order_page.select_black_color()
            order_page.fill_comment(comment_text=comment)

        with allure.step("Подтвердить и оформить заказ"):
            order_page.click_order_button()
            order_page.click_place_order_yes_button()

        with allure.step("Проверить, что заказ оформлен"):
            actual_order = order_page.get_order_number_text()
            assert 'Номер заказа' in actual_order

    @allure.story("Переход по логотипу Самокат")
    @allure.title("Проверка перехода по логотипу Самокат")
    def test_logo_samokat(self):
        with allure.step("Открыть главную страницу"):
            self.driver.get('https://qa-scooter.praktikum-services.ru/')

        main_page = MainPage(self.driver)
        order_page = OrderPage(self.driver)

        with allure.step("Нажать кнопку заказа снизу"):
            main_page.scroll_to_bottom_button()
            main_page.click_order_bottom_button()
            order_page.check_header_for_rent()

        with allure.step("Нажать на логотип Самокат"):
            order_page.click_samokat_logo()

        with allure.step("Проверить, что мы остались на главной странице"):
            assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
