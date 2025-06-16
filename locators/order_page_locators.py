from selenium.webdriver.common.by import By


class OrderPageLocators:
    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    INPUT_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO = (By.CSS_SELECTOR, "input.select-search__input[placeholder='* Станция метро']")
    INPUT_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    
    SAMOKAT_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter__3lsAR')]")
    NEXT_BTN = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Далее']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[contains(text(), 'Заказать')]")
    PLACE_ORDER_YES_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[contains(@class, 'Button_Middle__1CSJM') and text()='Да']")
    
    FOR_RENT = (By.XPATH, "//div[contains(@class, 'Order_Header__BZXOb') and text()='Для кого самокат']")
    ABOUT_RENT = (By.XPATH, "//div[contains(@class, 'Order_Header__BZXOb') and text()='Про аренду']")
    ORDER_NUMBER_BLOCK = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]/div[contains(@class, 'Order_Text')]")
    
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    BLACK_COLOR_CHECKBOX = (By.ID, "black")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    @staticmethod
    def get_day_locator(day):
        return (By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='{day}']")
    
    @staticmethod
    def get_period_locator(period):
        return (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{period}']")
    
    @staticmethod
    def get_metro_option_locator(metro_station):
        return (By.XPATH, f"//button[contains(@class, 'select-search__option')]//div[text()='{metro_station}']")