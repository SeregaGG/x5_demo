import json

import pytest

from framework.webdriver_manager import init_driver, close_driver, init_driver_if_not_open
from framework.utils import screen_for_allure_on_fail, screen_for_allure
import os

@pytest.fixture()
def search_params():
    # params = {
    #     'genre': ['боевик', 'биография', 'военный'],
    #     'title': 'Веном',
    #     'country': 'США'
    # }
    path = '../../framework/resources/test_params/search_data.json'
    path = os.path.join(os.path.dirname(__file__), path)
    with open(path, 'r', encoding='utf-8') as fp:
        params = json.load(fp)
    return params


@pytest.fixture(scope='session', autouse=True)
def setup_driver(request):
    init_driver(request.config)
    request.addfinalizer(close_driver)


@pytest.fixture(autouse=True)
def setup_driver_if_not_open(request):
    init_driver_if_not_open(request.config)


@pytest.fixture()
def close_driver_after_test(request):
    request.addfinalizer(close_driver)


@pytest.fixture
def allure_screen(request):
    yield
    screen_for_allure()


def pytest_exception_interact(node, call, report):
    screen_for_allure_on_fail()
