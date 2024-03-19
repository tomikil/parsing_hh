import src.utils as utils

words = ['английского']
salary = '10000-160000'


def test_filtered_vacancies(vacancies):
    vacancy = utils.filtered_vacancies(vacancies, words)
    assert vacancy[0].name == 'Junior Программист/Разработчик Python'
    assert vacancy[0].requirement == 'Знание английского языка ...'


def test_get_vacancies_by_salary(vacancies):
    vacancy = utils.get_vacancies_by_salary(utils.filtered_vacancies(vacancies, words), salary)
    assert vacancy[0].name == 'Junior Программист/Разработчик Python'


def test_sort_vacancies(vacancies):
    vacancy = utils.sort_vacancies(utils.get_vacancies_by_salary(utils.filtered_vacancies(vacancies, words), salary))
    assert vacancy[1].salary == '10000-60000'


def test_get_top_vacancies(vacancies):
    vacancies = utils.get_top_vacancies(
        utils.sort_vacancies(utils.get_vacancies_by_salary(utils.filtered_vacancies(vacancies, words), salary)), 2)
    assert vacancies[1].name == 'Junior Программист/Разработчик Python'
