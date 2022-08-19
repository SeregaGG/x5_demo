from selene.support import by
from selene.support.conditions import be
from selene.support.jquery_style_selectors import s
from selenium.webdriver.common.by import By
from framework.utils import attach_allure_screen


class FilmsPage:

    def __init__(self):
        self._films_block = s(
            by.xpath('//*[@id="block_left_pad"]/div/div[@class="search_results search_results_last"]'))
        self._most_likely_film = s(by.xpath('//*[@id="block_left_pad"]/div/div[2]/div/div/p/a'))

    def chek_top_five(self, title):

        if self._most_likely_film.text == title:
            return True

        top_five = self._films_block.find_elements(By.XPATH, './/div[position() >= 2][position() <= 5]/div/p/a')
        titles_list = [x.text.lower() for x in top_five]
        attach_allure_screen(self._films_block, attach_name='Блок с фильмами')
        return title in titles_list
