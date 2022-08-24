import typing

import allure
import pytest
from framework.ui_pages.kino_search_page import SearchPage
import os
import json
from hamcrest import assert_that
from hamcrest.library.collection.issequence_containing import has_item


@pytest.fixture()
def search_params():
    path = '../../framework/resources/test_params/search_data.json'
    path = os.path.join(os.path.dirname(__file__), path)
    with open(path, 'r', encoding='utf-8') as fp:
        params = json.load(fp)
    return params


@pytest.mark.positive
@pytest.mark.usefixtures('allure_screen')
@allure.feature('Тест заполнения')
class TestKinoForm:

    @allure.story('Заполнить форму')
    @allure.testcase('https://www.kinopoisk.ru/s/', name='Ссылка на тест-кейс')
    @pytest.mark.usefixtures("close_driver_after_test", 'search_params')
    def test_fill_block(self, search_params):
        main_page = SearchPage().open()
        films_page = main_page.search_film(**search_params)
        top = search_params.get('top')
        films_list: typing.Sequence = [x.lower() for x in films_page.get_films_list()][:top]
        title = search_params.get('title').lower()
        assert_that(films_list, has_item(title))  # typing.Sequence on 31 row for IDE (works without it)
