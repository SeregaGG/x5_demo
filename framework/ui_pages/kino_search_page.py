import selene.factory
import allure
from selene.support import by
from selene.browser import open_url
from selene.support.jquery_style_selectors import s
from framework.utils import attach_allure_screen
from selenium.webdriver.support.select import Select
from .films_page import FilmsPage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class SearchPage:
    GENRES_LIMIT = 3
    DEFAULT_VALUE = '-'

    def __init__(self):
        self._form_search_main = s(by.xpath('//form[@id="formSearchMain"]'))  # block for screen
        self._title_field = s(by.xpath('//input[@id="find_film"]'))  # input type
        self._country_selector = s(by.xpath('//select[@id="country"]'))  # select type
        self._genre_selector = s(by.xpath('//select[@id="m_act[genre]"]'))  # select type
        self._search_button = s(by.xpath('//form[@id="formSearchMain"]/input[@type="button" and @value="поиск"]'))

    @allure.step('Заполнение поля поиска по имени')
    def _fill_title_field(self, title):
        self._title_field.send_keys(title)
        attach_allure_screen(self._form_search_main, attach_name=f'Поиск по названию - {title}')

    @allure.step('Выбор страны')
    def _select_country(self, country):
        select_country_obj = Select(self._country_selector)
        select_country_obj.select_by_visible_text(country)
        if not country == self.DEFAULT_VALUE:
            attach_allure_screen(self._form_search_main, attach_name=f'Поиск по стране - {country}')

    @allure.step('Выбор жанров')
    def _select_genres(self, genres):
        if not genres == self.DEFAULT_VALUE:
            if len(genres) > self.GENRES_LIMIT:
                genres = genres[0:self.GENRES_LIMIT]

            for genre in genres:
                select_genre_obj = Select(self._genre_selector)
                select_genre_obj.select_by_visible_text(genre)
                attach_allure_screen(self._form_search_main, attach_name=f'Добавлен жанр - {genre}')

    @allure.step('Заполнение блока')
    def search_film(self, **kwargs):

        self._fill_title_field(kwargs.get('title'))

        self._select_country(kwargs.get('country', self.DEFAULT_VALUE))

        self._select_genres(kwargs.get('genre', self.DEFAULT_VALUE))

        attach_allure_screen(self._form_search_main, attach_name='Готовый блок')

        self._search_button.click()

        films_page = FilmsPage()

        return films_page

    def open(self):
        open_url('/')
        return self
