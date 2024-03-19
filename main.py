from src.head_hunter_api import HeadHunterAPI
from src.vacancy import Vacancy
from src.json_saver import JSONSaver
import src.utils as utils

url = 'https://api.hh.ru/vacancies'
file = 'data/vacancy.json'


def user_interaction():
    hp_ip = HeadHunterAPI(url)
    search_query = input("Введите поисковый запрос: ")
    hh_vacancies = hp_ip.get_vacancies(search_query)
    json_saver = JSONSaver()
    json_saver_vacancies = json_saver.get_list_vacancy(hh_vacancies)
    json_saver.add_vacancy(json_saver_vacancies, file)
    vacancies_list = Vacancy.get_list_object(json_saver.get_vacancies_json(file))
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split(' ')
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000
    filtered_vacancies = utils.filtered_vacancies(vacancies_list, filter_words)
    ranged_vacancies = utils.get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = utils.sort_vacancies(ranged_vacancies)
    top_vacancies = utils.get_top_vacancies(sorted_vacancies, top_n)
    utils.print_vacancies(top_vacancies)
    json_saver.delete_vacancy(file)


if __name__ == '__main__':
    user_interaction()
