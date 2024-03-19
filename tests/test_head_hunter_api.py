import pytest
from src.head_hunter_api import HeadHunterAPI

url = 'https://api.hh.ru/vacancies'
hh_api = HeadHunterAPI(url)


def test_init():
    assert hh_api.url == 'https://api.hh.ru/vacancies'


def test_connect():
    assert hh_api.connect() == 200


def test_get_vacancies():
    assert len(hh_api.get_vacancies('python')) == 4
