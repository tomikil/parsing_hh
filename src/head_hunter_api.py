import time
import requests
from src.abstract_head_hunter_api import HeadHunterAPIAbstract


class HeadHunterAPI(HeadHunterAPIAbstract):
    """
    Класс для подлючение к сервису поиска вакансий
    """
    def __init__(self, url):
        self.url = url

    def connect(self):
        """
        Функция реализует подключение к сервисц hh.ru и возвращает статус подключения
        :return:
        """
        response = requests.get(self.url)
        return response.status_code

    def get_vacancies(self, vacancy):
        """
        Функция возвращает список вакансий полученые с hh.ru
        :param vacancy:
        :return:
        """
        try:
            if self.connect() != 200:
                raise NameError(f"Ошибка подключения, статус ошибки: {self.connect()}")
            else:
                list_vacancies = []
                for page in range(0, 20):
                    response = requests.get(self.url, params={'text': vacancy, 'area': 4, 'page': page, 'per_page': 100})
                    vacancies = response.json()['items']
                    list_vacancies.append(vacancies)
                    if (response.json()['pages'] - page) <= 1:
                        break
                    time.sleep(0.25)
                return list_vacancies
        except NameError:
            print(NameError)
