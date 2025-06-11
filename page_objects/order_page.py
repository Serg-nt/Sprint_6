from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as es


class OrderPage:
    
    INPUT_NAME = [By.XPATH, "//input[@placeholder='* Имя']"]
    INPUT_SURNAME = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    INPUT_ADDRESS = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    INPUT_METRO = [By.CSS_SELECTOR, "input.select-search__input[placeholder='* Станция метро']"]
    INPUT_PHONE = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]

    SAMOKAT_LOGO = [By.XPATH, "//a[contains(@class, 'Header_LogoScooter__3lsAR')]"]

    NEXT_BTN = [By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Далее']"]
    ORDER_BUTTON = [By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[contains(text(), 'Заказать')]"]
    PLACE_ORDER_YES_BUTTON = [By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[contains(@class, 'Button_Middle__1CSJM') and text()='Да']"]

    FOR_RENT = [By.XPATH, "//div[contains(@class, 'Order_Header__BZXOb') and text()='Для кого самокат']"]
    ABOUT_RENT = [By.XPATH, "//div[contains(@class, 'Order_Header__BZXOb') and text()='Про аренду']"]
    ORDER_NUMBER_BLOCK = [By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]/div[contains(@class, 'Order_Text')]"]


    DATE_INPUT = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    RENT_PERIOD_DROPDOWN = [By.CLASS_NAME, "Dropdown-control"]
    BLACK_COLOR_CHECKBOX = [By.ID, "black"]
    COMMENT_INPUT = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]



    def __init__(self, driver):
        self.driver = driver

    def fill_name(self, name: str):
        self.driver.find_element(*self.INPUT_NAME).send_keys(name)

    def fill_surname(self, surname: str):
        self.driver.find_element(*self.INPUT_SURNAME).send_keys(surname)

    def fill_address(self, address: str):
        self.driver.find_element(*self.INPUT_ADDRESS).send_keys(address)

    def click_metro(self):
        self.driver.find_element(*self.INPUT_METRO).click()

    def select_metro_option_by_name(self, metro_station: str):
        self.click_metro()
        option_locator = (
            By.XPATH,
            f"//button[contains(@class, 'select-search__option')]//div[text()='{metro_station}']"
        )
        WebDriverWait(self.driver, 5).until(es.element_to_be_clickable(option_locator)).click()

    def fill_phone(self, phone: str):
        self.driver.find_element(*self.INPUT_PHONE).send_keys(phone)

    def check_header_for_rent(self):
        WebDriverWait(self.driver, 10).until(
            es.visibility_of_element_located(self.FOR_RENT)
        )

    def check_header_about_rent(self):
        WebDriverWait(self.driver, 5).until(
            es.visibility_of_element_located(self.ABOUT_RENT)
        )

    def click_next_is_enabled(self):
        self.driver.find_element(*self.NEXT_BTN).click()

    def select_date(self, day: int = 11):
        # Клик по полю даты, чтобы открылся календарь
        self.driver.find_element(*self.DATE_INPUT).click()

        # Локатор нужного дня в календаре — ищем div с текстом дня и классом react-datepicker__day
        day_locator = (By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='{day}']")
        
        # Ждем, что день появится и кликаем по нему
        WebDriverWait(self.driver, 10).until(
            es.element_to_be_clickable(day_locator)
        ).click()

    def select_rent_period(self, option_text="трое суток"):
        self.driver.find_element(*self.RENT_PERIOD_DROPDOWN).click()
        option_locator = (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{option_text}']")
        WebDriverWait(self.driver, 10).until(
            es.element_to_be_clickable(option_locator)
        ).click()

    def select_black_color(self):
        checkbox = self.driver.find_element(*self.BLACK_COLOR_CHECKBOX)
        if not checkbox.is_selected():
            checkbox.click()

    def fill_comment(self, comment_text="Комментарий1"):
        self.driver.find_element(*self.COMMENT_INPUT).send_keys(comment_text)

    def click_order_button(self):
        self.driver.find_element(*self.ORDER_BUTTON).click()

    def click_place_order_yes_button(self):
        WebDriverWait(self.driver, 10).until(
            es.element_to_be_clickable(self.PLACE_ORDER_YES_BUTTON)
        ).click()

    def get_order_number_text(self):
        return WebDriverWait(self.driver, 10).until(
        es.visibility_of_element_located(self.ORDER_NUMBER_BLOCK)
    ).text

    def click_samokat_logo(self):
        self.driver.find_element(*self.SAMOKAT_LOGO).click()
 