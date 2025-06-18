import allure
from .base_page import BasePage
from ..locators.main_page_locators import MainPageLocators
from ..urls import MAIN_PAGE_URL


class MainPage(BasePage):

    @allure.step("Скролл к вопросу")
    def scroll_to_question(self, locator):
        self.scroll_to_element(locator)

    @allure.step("Клик на вопрос")
    def click_question_when_clickable(self, locator):
        self.click_element(locator)

    @allure.step("Проверка видимости ответа")
    def check_for_answer_visible(self, locator):
        self.wait_for_element_visible(locator)

    @allure.step("Клик на кнопку 'Заказать' в хедере")
    def click_order_header_button(self):
        self.click_element(MainPageLocators.ORDER_HEADER_BTN)

    @allure.step("Клик на кнопку 'Заказать' внизу страницы")
    def click_order_bottom_button(self):
        self.scroll_to_element(MainPageLocators.ORDER_BOTTOM_BTN)
        self.click_element(MainPageLocators.ORDER_BOTTOM_BTN)

    @allure.step("Скролл к кнопке заказа в хедере")
    def scroll_to_header_button(self):
        self.scroll_to_element(MainPageLocators.ORDER_HEADER_BTN)

    @allure.step("Скролл к кнопке заказа внизу страницы")
    def scroll_to_bottom_button(self):
        self.scroll_to_element(MainPageLocators.ORDER_BOTTOM_BTN)

    @allure.step("Получение текста ответа")
    def get_answer_text(self, locator):
        return self.get_element_text(locator)

    @allure.step("Клик на логотип Яндекс")
    def click_logo_yandex(self):
        self.click_element(MainPageLocators.YA_LOGO)

    @allure.step("Открытие главной страницы")
    def open(self):
        self.open_url(MAIN_PAGE_URL)

    @allure.step("Проверка что открыта главная страница")
    def is_main_page(self):
        return self.get_current_url() == MAIN_PAGE_URL

    @allure.step("Проверка открытия страницы Dzen")
    def verify_dzen_opened(self):
        self.switch_to_new_tab()
        self.wait_for_url_contains("dzen.ru")
        return self.get_current_url()
