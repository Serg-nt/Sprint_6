from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as es


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_element_presence(self, locator):
        return self.wait.until(es.presence_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        return self.wait.until(es.element_to_be_clickable(locator))

    def wait_for_element_visible(self, locator):
        return self.wait.until(es.visibility_of_element_located(locator))

    def scroll_to_element(self, locator):
        element = self.wait_for_element_presence(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def click_element(self, locator):
        self.wait_for_element_clickable(locator).click()

    def send_keys_to_element(self, locator, text):
        self.wait_for_element_visible(locator).send_keys(text)

    def get_element_text(self, locator):
        return self.wait_for_element_visible(locator).text

    def switch_to_new_tab(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def wait_for_url_contains(self, text):
        self.wait.until(es.url_contains(text))

    def get_current_url(self):
        return self.driver.current_url

    def open_url(self, url: str):
        self.driver.get(url)
