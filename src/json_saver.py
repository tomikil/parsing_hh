import json
from src.abstract_json_saver import JSONSaverAbstract
import re


class JSONSaver(JSONSaverAbstract):
    def get_list_vacancy(self, vacancies):
        """
        Создания списка словарей вакансий для записи в файл
        :param vacancies: Словарь с вакансий с сайта hh.ru
        :return:
        """
        list_vacancy = []
        for item in range(0, len(vacancies)):
            for vacancy in vacancies[item]:
                salary = ''
                if vacancy['salary'] is None:
                    salary = "Зарплата не указана"
                elif vacancy['salary']['from'] is None:
                    salary = f"0-{vacancy['salary']['to']}"
                elif vacancy['salary']['to'] is None:
                    salary = f"{vacancy['salary']['from']}-0"
                else:
                    salary = f"{vacancy['salary']['from']}-{vacancy['salary']['to']}"

                list_vacancy.append({
                    "name": vacancy['name'],
                    "url": vacancy['alternate_url'],
                    "city": vacancy['area']['name'],
                    "salary": salary,
                    "requirement": re.sub(r'<.*?>', '', str(vacancy['snippet']['requirement'])),
                    "description": vacancy['snippet']['responsibility']

                })
        return list_vacancy

    def add_vacancy(self, list_vacancy, file):
        """
        Запись списка вакансий в файл JSON
        :param file: наименование json файла для записи вакансий
        :param list_vacancy: Список словарей вакансий
        :return:
        """
        file = open(file, 'w', encoding='utf8')
        file.write(json.dumps(list_vacancy, ensure_ascii=False, indent=2))
        file.close()

    def delete_vacancy(self, files):
        """
        Удаление вакансий из файла json
        :return:
        """
        with open(files, 'w') as file:
            file.write('')

    @staticmethod
    def get_vacancies_json(files):
        """
        Чтение вакансий из файла json
        :param files: Наименование файла json
        :return:
        """
        with open(files, encoding='utf8') as file:
            return json.load(file)
