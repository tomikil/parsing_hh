from src.json_saver import JSONSaver
import json

files = './data/vacancy.json'
json_saver = JSONSaver()


def test_get_list_vacancy(get_vacancies):
    assert json_saver.get_list_vacancy(get_vacancies)[0]['salary'] == '100000-0'
    assert json_saver.get_list_vacancy(get_vacancies)[1]['salary'] == '0-60000'
    assert json_saver.get_list_vacancy(get_vacancies)[2]['salary'] == '40000-70000'
    assert json_saver.get_list_vacancy(get_vacancies)[3]['salary'] == 'Зарплата не указана'


def test_add_vacancy(get_vacancies):
    json_saver.add_vacancy(json_saver.get_list_vacancy(get_vacancies), files)
    with open(files, 'r', encoding='UTF-8') as file:
        vacancies = json.load(file)
        assert len(vacancies) == 4
        assert vacancies[1]['salary'] == '0-60000'


def test_get_vacancies_json():
    vacancy = json_saver.get_vacancies_json(files)
    assert vacancy[0]['name'] == 'Тестировщик'


def test_delete_vacancy(get_vacancies):
    JSONSaver.delete_vacancy(json_saver, files)
    with open(files, 'r', encoding='UTF-8') as file:
        vacancies = file.read()
        assert len(vacancies) == 0
