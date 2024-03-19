from src.vacancy import Vacancy


def test_init(vacancies):
    assert vacancies[0].name == 'Тестировщик'
    assert vacancies[0].url_vacancy == 'url'
    assert vacancies[0].salary == '100000-0'
    assert vacancies[0].city == 'Новосибирск'
    assert vacancies[0].requirement == 'Знания веб-технологий ...'
    assert vacancies[0].description == 'Ручное функциональное тестирование ...'


def test_str(vacancies):
    assert vacancies[1].__str__() == ('Junior Программист/Разработчик Python\n'
                                      'Зарплата: 10000-60000 руб.\n'
                                      'Требование: Знание английского языка ...\n'
                                      'Описание: Разработка, тестирование, отладка ...\n'
                                      'Ссылка на вакансию: url')


def test_gt(vacancies):
    salary = vacancies[0] > vacancies[1]
    assert salary is True


def test_get_list_object(vacancies_list):
    vacancy = Vacancy.get_list_object(vacancies_list)
    assert vacancy[2].name == 'Программист'
