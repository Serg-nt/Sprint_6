import allure
import pytest
from ..page_objects.main_page import MainPage
from ..data.main_page_data import test_data


@allure.epic("Тесты главной страницы")
@pytest.mark.usefixtures("driver")
class TestMainPage:

    @pytest.mark.parametrize("question_locator,answer_locator,expected_answer", test_data)
    @allure.feature("Блок 'Вопросы о важном'")
    @allure.story("Контент вопросов и ответов")
    @allure.title("Проверка корректности информации")
    def test_important_questions(self, question_locator, answer_locator, expected_answer):
        main_page = MainPage(self.driver)

        with allure.step("Открыть главную страницу"):
            main_page.open()
        
        with allure.step(f"Пролистать к вопросу с локатором {question_locator}"):
            main_page.scroll_to_question(question_locator)
        
        with allure.step(f"Кликнуть на вопрос с локатором {question_locator}"):
            main_page.click_question_when_clickable(question_locator)
        
        with allure.step(f"Проверить видимость ответа с локатором {answer_locator}"):
            main_page.check_for_answer_visible(answer_locator)
        
        with allure.step("Сравнить текст ответа с ожидаемым"):
            actual_answer = main_page.get_answer_text(answer_locator)
            assert actual_answer == expected_answer

    @allure.feature("Логотипы")
    @allure.story("Переход по логотипу Яндекса")
    @allure.title("Переход на dzen.ru при нажатии логотипа Яндекс")
    def test_logo_yandex(self):
        main_page = MainPage(self.driver)
        
        with allure.step("Открыть главную страницу"):
            main_page.open()
        
        with allure.step("Кликнуть на логотип Яндекс"):
            main_page.click_logo_yandex()
        
        with allure.step("Проверить переход на dzen.ru"):
            current_url = main_page.verify_dzen_opened()
            assert "dzen.ru" in current_url
