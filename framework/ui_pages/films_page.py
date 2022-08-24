from selene.support import by
from selene.support.jquery_style_selectors import s
from selenium.webdriver.common.by import By
from framework.utils import attach_allure_screen


class FilmsPage:

    def __init__(self):
        self._films_block = s(by.xpath('//table/tbody'))

    def get_films_list(self):
        films = self._films_block.find_elements(By.XPATH, f'.//div/p[@class="name"]/a')
        attach_allure_screen(self._films_block, attach_name='Блок с фильмами')
        titles_list = [x.text for x in films]
        return titles_list
