from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as es


class MainPage:
    ORDER_HEADER_BTN = [By.XPATH, "//div[contains(@class,'Header_Nav')]/button[text()='Заказать']"]
    ORDER_BOTTOM_BTN = [By.XPATH, "//div[contains(@class,'Home_FinishButton')]/button[text()='Заказать']"]

    YA_LOGO = [By.CLASS_NAME, "Header_LogoYandex__3TSOI"]

    QUESTION_COST = [By.ID, "accordion__heading-0"]
    QUESTION_MULTIPLE_SCOOTERS = [By.ID, "accordion__heading-1"]
    QUESTION_RENT_TIME = [By.ID, "accordion__heading-2"]
    QUESTION_TODAY_ORDER = [By.ID, "accordion__heading-3"]
    QUESTION_EXTEND_RETURN = [By.ID, "accordion__heading-4"]
    QUESTION_CHARGER = [By.ID, "accordion__heading-5"]
    QUESTION_CANCEL_ORDER = [By.ID, "accordion__heading-6"]
    QUESTION_OUTSIDE_MKAD = [By.ID, "accordion__heading-7"]

    ANSWER_COST = [By.ID, "accordion__panel-0"]
    ANSWER_MULTIPLE_SCOOTERS = [By.ID, "accordion__panel-1"]
    ANSWER_RENT_TIME = [By.ID, "accordion__panel-2"]
    ANSWER_TODAY_ORDER = [By.ID, "accordion__panel-3"]
    ANSWER_EXTEND_RETURN = [By.ID, "accordion__panel-4"]
    ANSWER_CHARGER = [By.ID, "accordion__panel-5"]
    ANSWER_CANCEL_ORDER = [By.ID, "accordion__panel-6"]
    ANSWER_OUTSIDE_MKAD = [By.ID, "accordion__panel-7"]

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_question(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            es.presence_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def click_question_when_clickable(self, locator):
        WebDriverWait(self.driver, 5).until(
            es.element_to_be_clickable(locator)
        ).click()

    def check_for_answer_visible(self, locator):
        WebDriverWait(self.driver, 5).until(
            es.visibility_of_element_located(locator)
        )

    def click_order_header_button(self):
        self.driver.find_element(*self.ORDER_HEADER_BTN).click()

    def click_order_bottom_button(self):
        self.driver.find_element(*self.ORDER_BOTTOM_BTN).click()

    def scroll_to_header_button(self):
        element = WebDriverWait(self.driver, 10).until(
            es.presence_of_element_located(self.ORDER_HEADER_BTN)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def scroll_to_bottom_button(self):
        element = WebDriverWait(self.driver, 10).until(
            es.presence_of_element_located(self.ORDER_BOTTOM_BTN)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def get_answer_text(self, locator):
        return self.driver.find_element(*locator).text

    def click_logo_yandex(self):
        self.driver.find_element(*self.YA_LOGO).click()

    def check_for_new_tab(self):
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def check_for_url_dzen(self):
        WebDriverWait(self.driver, 10).until(es.url_contains("dzen.ru"))