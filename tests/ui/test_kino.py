import allure
import pytest
from framework.ui_pages.kino_search_page import SearchPage


@pytest.mark.positive
@pytest.mark.usefixtures('allure_screen')
@allure.feature('Тест заполнения')
class TestKinoForm:

    @allure.story('Зполнить форму')
    @allure.testcase('https://www.kinopoisk.ru/s/', name='Ссылка на тест-кейс')
    @pytest.mark.usefixtures("close_driver_after_test", 'search_params')
    def test_fill_block(self, search_params):
        main_page = SearchPage().open()
        films_page = main_page.search_film(**search_params)
        assert films_page.chek_top_five(search_params.get('title').lower())

