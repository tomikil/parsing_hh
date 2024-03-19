import pytest
from src.vacancy import Vacancy

vacancy = [[{'id': '94759534', 'premium': False, 'name': 'Тестировщик', 'department': None, 'has_test': False,
             'response_letter_required': False,
             'area': {'id': '4', 'name': 'Новосибирск', 'url': 'https://api.hh.ru/areas/4'},
             'salary': {'from': 100000, 'to': None, 'currency': 'RUR', 'gross': True},
             'type': {'id': 'open', 'name': 'Открытая'}, 'address': {'city': 'Новосибирск',
                                                                     'street': 'Советский район, микрорайон Академгородок, проспект Академика Лаврентьева',
                                                                     'building': '6/1', 'lat': 54.851163,
                                                                     'lng': 83.100632, 'description': None,
                                                                     'raw': 'Новосибирск, Советский район, микрорайон Академгородок, проспект Академика Лаврентьева, 6/1',
                                                                     'metro': None, 'metro_stations': [],
                                                                     'id': '14740610'}, 'response_url': None,
             'sort_point_distance': None, 'published_at': '2024-03-14T13:09:15+0300',
             'created_at': '2024-03-14T13:09:15+0300', 'archived': False,
             'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=94759534',
             'show_logo_in_search': None, 'insider_interview': None,
             'url': 'https://api.hh.ru/vacancies/94759534?host=hh.ru',
             'alternate_url': 'https://hh.ru/vacancy/94759534',
             'relations': [],
             'employer': {'id': '876275', 'name': 'Стилсофт', 'url': 'https://api.hh.ru/employers/876275',
                          'alternate_url': 'https://hh.ru/employer/876275',
                          'logo_urls': {'90': 'https://img.hhcdn.ru/employer-logo/6255578.jpeg',
                                        'original': 'https://img.hhcdn.ru/employer-logo-original/1158782.jpg',
                                        '240': 'https://img.hhcdn.ru/employer-logo/6255579.jpeg'},
                          'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=876275',
                          'accredited_it_employer': False, 'trusted': True}, 'snippet': {
        'requirement': 'Знания веб-технологий (html, css, js, http). Опыт работы с IP-телефонией. Опыт программирования на скриптовых языках (Bash, <highlighttext>Python</highlighttext>). ',
        'responsibility': 'Ручное функциональное тестирование web-проектов. Проведение тестирования (по тест-кейсам, чек-листам и методом свободного поиска). Разработка тест-планов, написание...'},
             'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
             'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
             'professional_roles': [{'id': '124', 'name': 'Тестировщик'}], 'accept_incomplete_resumes': False,
             'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
             'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None,
             'is_adv_vacancy': False,
             'adv_context': None},
            {'id': '94376365', 'premium': False, 'name': 'Junior Программист/Разработчик Python', 'department': None,
             'has_test': False, 'response_letter_required': False,
             'area': {'id': '4', 'name': 'Новосибирск', 'url': 'https://api.hh.ru/areas/4'},
             'salary': {'from': None, 'to': 60000, 'currency': 'RUR', 'gross': False},
             'type': {'id': 'open', 'name': 'Открытая'},
             'address': {'city': 'Новосибирск', 'street': 'улица Николаева', 'building': '12', 'lat': 54.857844,
                         'lng': 83.111798, 'description': None, 'raw': 'Новосибирск, улица Николаева, 12',
                         'metro': None,
                         'metro_stations': [], 'id': '3724874'}, 'response_url': None, 'sort_point_distance': None,
             'published_at': '2024-03-16T06:41:54+0300', 'created_at': '2024-03-16T06:41:54+0300', 'archived': False,
             'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=94376365',
             'show_logo_in_search': None, 'insider_interview': None,
             'url': 'https://api.hh.ru/vacancies/94376365?host=hh.ru',
             'alternate_url': 'https://hh.ru/vacancy/94376365',
             'relations': [],
             'employer': {'id': '2326492', 'name': 'Телеком-Инжиниринг', 'url': 'https://api.hh.ru/employers/2326492',
                          'alternate_url': 'https://hh.ru/employer/2326492',
                          'logo_urls': {'240': 'https://img.hhcdn.ru/employer-logo/1758863.png',
                                        'original': 'https://img.hhcdn.ru/employer-logo-original/329128.png',
                                        '90': 'https://img.hhcdn.ru/employer-logo/1758862.png'},
                          'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=2326492',
                          'accredited_it_employer': False, 'trusted': True}, 'snippet': {
                'requirement': 'Знание английского языка достаточное для чтения технической документации. Опыт разработки приложений на <highlighttext>Python</highlighttext>/Qt/C++/C#. Желателен опыт работы с.',
                'responsibility': 'Разработка, тестирование, отладка и поддержка кросс-платформенных (x86/ARM) приложений на <highlighttext>Python</highlighttext>.'},
             'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
             'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': True,
             'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}],
             'accept_incomplete_resumes': False, 'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
             'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None,
             'is_adv_vacancy': False,
             'adv_context': None},
            {'id': '94002763', 'premium': False, 'name': 'Программист', 'department': None, 'has_test': False,
             'response_letter_required': False,
             'area': {'id': '4', 'name': 'Новосибирск', 'url': 'https://api.hh.ru/areas/4'},
             'salary': {'from': 40000, 'to': 70000, 'currency': 'RUR', 'gross': False},
             'type': {'id': 'open', 'name': 'Открытая'},
             'address': {'city': 'Новосибирск', 'street': 'улица Ленина', 'building': '21/1к1', 'lat': 55.028739,
                         'lng': 82.905823, 'description': None, 'raw': 'Новосибирск, улица Ленина, 21/1к1',
                         'metro': None, 'metro_stations': [], 'id': '15261458'}, 'response_url': None,
             'sort_point_distance': None, 'published_at': '2024-02-29T07:57:17+0300',
             'created_at': '2024-02-29T07:57:17+0300', 'archived': False,
             'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=94002763',
             'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/94002763?host=hh.ru',
             'alternate_url': 'https://hh.ru/vacancy/94002763', 'relations': [],
             'employer': {'id': '9673749', 'name': 'Терехов Павел Владимирович',
                          'url': 'https://api.hh.ru/employers/9673749',
                          'alternate_url': 'https://hh.ru/employer/9673749', 'logo_urls': None,
                          'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=9673749',
                          'accredited_it_employer': False, 'trusted': True},
             'snippet': {'requirement': '<highlighttext>Python</highlighttext> (Pandos). VBA. MSSQL.',
                         'responsibility': 'Сопровождение продукта Visar.ru (дашборд). Разработка и сборка новых отчётов. Автоматизация существующих процессов.'},
             'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
             'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': True,
             'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}],
             'accept_incomplete_resumes': False, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
             'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None,
             'is_adv_vacancy': False,
             'adv_context': None},
            {'id': '94002763', 'premium': False, 'name': 'Программист', 'department': None, 'has_test': False,
             'response_letter_required': False,
             'area': {'id': '4', 'name': 'Новосибирск', 'url': 'https://api.hh.ru/areas/4'},
             'salary': None,
             'type': {'id': 'open', 'name': 'Открытая'},
             'address': {'city': 'Новосибирск', 'street': 'улица Ленина', 'building': '21/1к1', 'lat': 55.028739,
                         'lng': 82.905823, 'description': None, 'raw': 'Новосибирск, улица Ленина, 21/1к1',
                         'metro': None, 'metro_stations': [], 'id': '15261458'}, 'response_url': None,
             'sort_point_distance': None, 'published_at': '2024-02-29T07:57:17+0300',
             'created_at': '2024-02-29T07:57:17+0300', 'archived': False,
             'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=94002763',
             'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/94002763?host=hh.ru',
             'alternate_url': 'https://hh.ru/vacancy/94002763', 'relations': [],
             'employer': {'id': '9673749', 'name': 'Терехов Павел Владимирович',
                          'url': 'https://api.hh.ru/employers/9673749',
                          'alternate_url': 'https://hh.ru/employer/9673749', 'logo_urls': None,
                          'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=9673749',
                          'accredited_it_employer': False, 'trusted': True},
             'snippet': {'requirement': '<highlighttext>Python</highlighttext> (Pandos). VBA. MSSQL.',
                         'responsibility': 'Сопровождение продукта Visar.ru (дашборд). Разработка и сборка новых отчётов. Автоматизация существующих процессов.'},
             'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
             'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': True,
             'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}],
             'accept_incomplete_resumes': False, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
             'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None,
             'is_adv_vacancy': False,
             'adv_context': None}
            ]]

list_vacancies = [
    {
        "name": "Тестировщик",
        "url": "https://hh.ru/vacancy/94759534",
        "city": "Новосибирск",
        "salary": "100000-0",
        "requirement": "Знания веб-технологий (html, css, js, http). Опыт работы с IP-телефонией. Опыт программирования на скриптовых языках (Bash, Python). ",
        "description": "Ручное функциональное тестирование web-проектов. Проведение тестирования (по тест-кейсам, чек-листам и методом свободного поиска). Разработка тест-планов, написание..."
    },
    {
        "name": "Junior Программист/Разработчик Python",
        "url": "https://hh.ru/vacancy/94376365",
        "city": "Новосибирск",
        "salary": "0-60000",
        "requirement": "Знание английского языка достаточное для чтения технической документации. Опыт разработки приложений на Python/Qt/C++/C#. Желателен опыт работы с.",
        "description": "Разработка, тестирование, отладка и поддержка кросс-платформенных (x86/ARM) приложений на <highlighttext>Python</highlighttext>."
    },
    {
        "name": "Программист",
        "url": "https://hh.ru/vacancy/94002763",
        "city": "Новосибирск",
        "salary": "40000-70000",
        "requirement": "Python (Pandos). VBA. MSSQL.",
        "description": "Сопровождение продукта Visar.ru (дашборд). Разработка и сборка новых отчётов. Автоматизация существующих процессов."
    },
    {
        "name": "Программист",
        "url": "https://hh.ru/vacancy/94002763",
        "city": "Новосибирск",
        "salary": "Зарплата не указана",
        "requirement": "Python (Pandos). VBA. MSSQL.",
        "description": "Сопровождение продукта Visar.ru (дашборд). Разработка и сборка новых отчётов. Автоматизация существующих процессов."
    }
]


@pytest.fixture
def get_vacancies():
    return vacancy


@pytest.fixture
def vacancies():
    vacancy = [Vacancy('Тестировщик', 'url', 'Новосибирск', '100000-0',
                       'Знания веб-технологий ...', 'Ручное функциональное тестирование ...'),
               Vacancy('Junior Программист/Разработчик Python', 'url', 'Москва', '10000-60000',
                       'Знание английского языка ...', 'Разработка, тестирование, отладка ...'),
               Vacancy('Junior Разработчик Python', 'url', 'Саратов', 'Зарплата не указана',
                       'Знание английского языка ...', 'Разработка, тестирование, отладка ...'),
               Vacancy('Junior', 'url', 'Саратов', '50000-150000',
                       'Знание английского языка ...', 'Разработка, тестирование, отладка ...')
               ]
    return vacancy


@pytest.fixture
def vacancies_list():
    return list_vacancies



