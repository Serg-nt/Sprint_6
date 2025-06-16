from .base_page import BasePage
from ..locators.main_page_locators import MainPageLocators
from ..urls import MAIN_PAGE_URL


class MainPage(BasePage):

    def scroll_to_question(self, locator):
        self.scroll_to_element(locator)

    def click_question_when_clickable(self, locator):
        self.click_element(locator)

    def check_for_answer_visible(self, locator):
        self.wait_for_element_visible(locator)

    def click_order_header_button(self):
        self.click_element(MainPageLocators.ORDER_HEADER_BTN)

    def click_order_bottom_button(self):
        self.scroll_to_element(MainPageLocators.ORDER_BOTTOM_BTN)
        self.click_element(MainPageLocators.ORDER_BOTTOM_BTN)

    def scroll_to_header_button(self):
        self.scroll_to_element(MainPageLocators.ORDER_HEADER_BTN)

    def scroll_to_bottom_button(self):
        self.scroll_to_element(MainPageLocators.ORDER_BOTTOM_BTN)

    def get_answer_text(self, locator):
        return self.get_element_text(locator)

    def click_logo_yandex(self):
        self.click_element(MainPageLocators.YA_LOGO)

    def get_current_url(self):
        return super().get_current_url()

    def open(self):
        self.open_url(MAIN_PAGE_URL)

    def is_main_page(self):
        return self.get_current_url() == MAIN_PAGE_URL

    def verify_dzen_opened(self):
        self.switch_to_new_tab()
        self.wait_for_url_contains("dzen.ru")
        return self.get_current_url()
