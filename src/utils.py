def filtered_vacancies(vacancies_list, words):
    """
    Фенкция фильтрует вакансии по ключевым словам и возвращает список вакансий
    :param vacancies_list: Список с вакансиями
    :param words: Список с ключевыми словами
    :return:
    """
    filtered_list = []
    for vacancy in vacancies_list:
        requirement_lower = str(vacancy.requirement).lower()
        for word in words:
            if word.lower() in requirement_lower:
                filtered_list.append(vacancy)
    return filtered_list


def get_vacancies_by_salary(vacancies, salary_range):
    """
    Фцнкция фильтрует вакансии по заданному диапазону заплаты
    :param vacancies: Список вакансий
    :param salary_range: Заданный диапазоп зарплаты
    :return:
    """
    vacancies_list = []
    min_salary, max_salary = str(salary_range).split('-')
    for vacancy in vacancies:
        if vacancy.salary != 'Зарплата не указана':
            min_vacancy_salary, max_vacancy_salary = vacancy.salary.split('-')

            if int(min_salary) <= int(min_vacancy_salary) and int(max_salary) >= int(max_vacancy_salary):
                vacancies_list.append(vacancy)
    return vacancies_list


def sort_vacancies(vacancies):
    """
    Функция сортирует вакансии по зарплате по убыванию
    :param vacancies:
    :return:
    """
    sort_vacancy = sorted(vacancies, key=lambda x: x.salary, reverse=True)
    return sort_vacancy


def get_top_vacancies(vacancies, top_n):
    """
    Функция возвращает введеное N-е количество вакансий
    :param vacancies: Список вакансий
    :param top_n: Количество вакансий для вывода
    :return:
    """
    return vacancies[:top_n]


def print_vacancies(vacancies):
    """
    Функция печатает информацию об фильтрованных и сортированных вакансий
    :param vacancies:
    :return:
    """
    for vacancy in vacancies:
        print(vacancy)
