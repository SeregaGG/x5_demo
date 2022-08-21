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
        self._form_search_main = s(by.xpath('//*[@id="formSearchMain"]'))  # block for screen
        self._title_field = s(by.xpath('//*[@id="find_film"]'))  # input type
        self._country_selector = s(by.xpath('//*[@id="country"]'))  # select type
        self._genre_selector = s(by.xpath('//*[@id="m_act[genre]"]'))  # select type
        self._search_button = s(by.xpath('//*[@id="formSearchMain"]/input[@type="button"]'))

    @allure.step('Заполнение поля поиска по имени')
    def fill_title_field(self, title):
        self._title_field.send_keys(title)
        attach_allure_screen(self._form_search_main, attach_name=f'Поиск по названию - {title}')

    @allure.step('Выбор страны')
    def select_country(self, country):
        select_country_obj = Select(self._country_selector)
        select_country_obj.select_by_visible_text(country)
        if not country == self.DEFAULT_VALUE:
            attach_allure_screen(self._form_search_main, attach_name=f'Поиск по стране - {country}')

    @allure.step('Выбор жанров')
    def select_genres(self, genres):
        if not genres == self.DEFAULT_VALUE:
            if len(genres) > self.GENRES_LIMIT:
                genres = genres[0:self.GENRES_LIMIT]

            for genre in genres:
                select_genre_obj = Select(self._genre_selector)
                select_genre_obj.select_by_visible_text(genre)
                attach_allure_screen(self._form_search_main, attach_name=f'Добавлен жанр - {genre}')

    @allure.step('Заполнение блока')
    def search_film(self, **kwargs):

        self.fill_title_field(kwargs.get('title'))

        self.select_country(kwargs.get('country', self.DEFAULT_VALUE))

        self.select_genres(kwargs.get('genre', self.DEFAULT_VALUE))

        attach_allure_screen(self._form_search_main, attach_name='Готовый блок')

        self._search_button.click()

        films_page = FilmsPage()

        return films_page

    def open(self):
        open_url('/')
        return self
