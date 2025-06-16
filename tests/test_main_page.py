import allure
import pytest
from ..page_objects.main_page import MainPage
from .main_page_data import test_data


@allure.epic("Тесты главной страницы")
@pytest.mark.usefixtures("driver")
class TestMainPage:

    @pytest.mark.parametrize("question_locator,answer_locator,expected_answer", test_data)
    @allure.feature("Блок 'Вопросы о важном'")
    @allure.story("Контент вопросов и ответов")
    def test_important_questions(self, question_locator, answer_locator, expected_answer):
        main_page = MainPage(self.driver)
        main_page.open()
        
        main_page.scroll_to_question(question_locator)
        main_page.click_question_when_clickable(question_locator)
        main_page.check_for_answer_visible(answer_locator)
        
        actual_answer = main_page.get_answer_text(answer_locator)
        assert actual_answer == expected_answer

    @allure.feature("Логотипы")
    @allure.story("Переход по логотипу Яндекса")
    def test_logo_yandex(self):
        main_page = MainPage(self.driver)
        main_page.open()
        
        main_page.click_logo_yandex()
        current_url = main_page.verify_dzen_opened()

        assert "dzen.ru" in current_url
