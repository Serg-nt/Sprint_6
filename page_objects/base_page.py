from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Ожидание присутствия элемента {locator}")
    def wait_for_element_presence(self, locator):
        return self.wait.until(es.presence_of_element_located(locator))

    @allure.step("Ожидание кликабельности элемента {locator}")
    def wait_for_element_clickable(self, locator):
        return self.wait.until(es.element_to_be_clickable(locator))

    @allure.step("Ожидание видимости элемента {locator}")
    def wait_for_element_visible(self, locator):
        return self.wait.until(es.visibility_of_element_located(locator))

    @allure.step("Скролл к элементу {locator}")
    def scroll_to_element(self, locator):
        element = self.wait_for_element_presence(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Клик по элементу {locator}")
    def click_element(self, locator):
        self.wait_for_element_clickable(locator).click()

    @allure.step("Ввод текста '{text}' в элемент {locator}")
    def send_keys_to_element(self, locator, text):
        self.wait_for_element_visible(locator).send_keys(text)

    @allure.step("Получение текста элемента {locator}")
    def get_element_text(self, locator):
        return self.wait_for_element_visible(locator).text

    @allure.step("Переключение на новую вкладку")
    def switch_to_new_tab(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Ожидание URL содержащего '{text}'")
    def wait_for_url_contains(self, text):
        self.wait.until(es.url_contains(text))

    @allure.step("Открытие URL: {url}")
    def open_url(self, url: str):
        self.driver.get(url)

    @allure.step("Получение текущего URL")
    def get_current_url(self) -> str:
        return self.driver.current_url

    @allure.step("Проверка соответствия URL ожидаемому: {expected_url}")
    def is_current_url_matches(self, expected_url: str) -> bool:
        return self.get_current_url() == expected_url
