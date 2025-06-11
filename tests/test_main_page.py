import allure
import pytest
from selenium import webdriver
from ..page_objects.main_page import MainPage


@allure.epic("Тесты главной страницы")
class TestManePage:

    driver = None

    test_data = [
        (MainPage.QUESTION_COST, MainPage.ANSWER_COST,
         "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (MainPage.QUESTION_MULTIPLE_SCOOTERS, MainPage.ANSWER_MULTIPLE_SCOOTERS,
         "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        (MainPage.QUESTION_RENT_TIME, MainPage.ANSWER_RENT_TIME,
         "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        (MainPage.QUESTION_TODAY_ORDER, MainPage.ANSWER_TODAY_ORDER,
         "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        (MainPage.QUESTION_EXTEND_RETURN, MainPage.ANSWER_EXTEND_RETURN,
         "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        (MainPage.QUESTION_CHARGER, MainPage.ANSWER_CHARGER,
         "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
        (MainPage.QUESTION_CANCEL_ORDER, MainPage.ANSWER_CANCEL_ORDER,
         "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        (MainPage.QUESTION_OUTSIDE_MKAD, MainPage.ANSWER_OUTSIDE_MKAD,
         "Да, обязательно. Всем самокатов! И Москве, и Московской области."),
    ]

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize("question_locator,answer_locator,expected_answer", test_data)
    @allure.feature("Блок 'Вопросы о важном'")
    @allure.story("Контент вопросов и ответов")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Проверка вопроса: {expected_answer}")
    def test_important_questions(self, question_locator, answer_locator, expected_answer):
        with allure.step("Открываем главную страницу"):
            self.driver.get('https://qa-scooter.praktikum-services.ru/')
            main_page = MainPage(self.driver)

        with allure.step("Скроллим к вопросу"):
            main_page.scroll_to_question(question_locator)

        with allure.step("Кликаем по вопросу"):
            main_page.click_question_when_clickable(question_locator)

        with allure.step("Ждём отображения ответа"):
            main_page.check_for_answer_visible(answer_locator)

        with allure.step("Получаем текст ответа"):
            actual_answer = main_page.get_answer_text(answer_locator)

        with allure.step("Проверяем, что ответ соответствует ожидаемому"):
            assert actual_answer == expected_answer, (
                f"Текст ответа не совпадает. Ожидалось: '{expected_answer}', получено: '{actual_answer}'"
            )

    @allure.feature("Логотипы")
    @allure.story("Переход по логотипу Яндекса")
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("Переход по логотипу Яндекса ведёт на Dzen")
    def test_logo_yandex(self):
        with allure.step("Открываем главную страницу"):
            self.driver.get('https://qa-scooter.praktikum-services.ru/')
            main_page = MainPage(self.driver)

        with allure.step("Кликаем по логотипу Яндекса"):
            main_page.click_logo_yandex()

        with allure.step("Переходим на новую вкладку"):
            main_page.check_for_new_tab()
            main_page.switch_to_new_tab()

        with allure.step("Проверяем, что открыта страница Dzen"):
            main_page.check_for_url_dzen()
            assert "dzen.ru" in self.driver.current_url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
