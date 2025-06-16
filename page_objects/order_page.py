from .base_page import BasePage
from ..locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    def fill_name(self, name):
        self.send_keys_to_element(OrderPageLocators.INPUT_NAME, name)

    def fill_surname(self, surname):
        self.send_keys_to_element(OrderPageLocators.INPUT_SURNAME, surname)

    def fill_address(self, address):
        self.send_keys_to_element(OrderPageLocators.INPUT_ADDRESS, address)

    def fill_phone(self, phone):
        self.send_keys_to_element(OrderPageLocators.INPUT_PHONE, phone)

    def select_metro_station(self, metro_station):
        self.click_element(OrderPageLocators.INPUT_METRO)
        self.click_element(OrderPageLocators.get_metro_option_locator(metro_station))

    def click_next_button(self):
        self.scroll_to_element(OrderPageLocators.NEXT_BTN)
        self.click_element(OrderPageLocators.NEXT_BTN)

    def select_date(self, day):
        self.scroll_to_element(OrderPageLocators.DATE_INPUT)
        self.click_element(OrderPageLocators.DATE_INPUT)
        self.click_element(OrderPageLocators.get_day_locator(day))

    def select_rent_period(self, period):
        self.scroll_to_element(OrderPageLocators.RENT_PERIOD_DROPDOWN)
        self.click_element(OrderPageLocators.RENT_PERIOD_DROPDOWN)
        self.click_element(OrderPageLocators.get_period_locator(period))

    def select_black_color(self):
        self.scroll_to_element(OrderPageLocators.BLACK_COLOR_CHECKBOX)
        self.click_element(OrderPageLocators.BLACK_COLOR_CHECKBOX)

    def fill_comment(self, comment):
        self.scroll_to_element(OrderPageLocators.COMMENT_INPUT)
        self.send_keys_to_element(OrderPageLocators.COMMENT_INPUT, comment)

    def click_order_button(self):
        self.scroll_to_element(OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    def confirm_order(self):
        self.scroll_to_element(OrderPageLocators.PLACE_ORDER_YES_BUTTON)
        self.click_element(OrderPageLocators.PLACE_ORDER_YES_BUTTON)

    def get_order_number_text(self):
        return self.get_element_text(OrderPageLocators.ORDER_NUMBER_BLOCK)

    def click_samokat_logo(self):
        self.scroll_to_element(OrderPageLocators.SAMOKAT_LOGO)
        self.click_element(OrderPageLocators.SAMOKAT_LOGO)

    def is_for_rent_header_visible(self):
        return self.wait_for_element_visible(OrderPageLocators.FOR_RENT)
