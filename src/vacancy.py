class Vacancy:
    def __init__(self, name, url_vacancy, city, salary, requirement, description):
        self.name = name
        self.url_vacancy = url_vacancy
        self.city = city
        self.salary = salary
        self.requirement = requirement
        self.description = description

    def __str__(self):
        """
        Магический метод для отображения информации о вакансиях
        :return:
        """
        return (f"{self.name}\nЗарплата: {self.salary} руб.\nТребование: {self.requirement}\n"
                f"Описание: {self.description}\n"
                f"Ссылка на вакансию: {self.url_vacancy}")

    def __gt__(self, other):
        """
        Магический метод для проверяет какой из обьектов больше по зарплате
        :param other: обьект класса с которым сравнивать
        :return:
        """
        salary_min, salary_max = self.salary.split('-')
        other_min, other_max = other.salary.split('-')
        return salary_min > other_min

    @classmethod
    def get_list_object(cls, vacancies):
        """
        Класс метод создания нового обьекта класса
        :param vacancies:
        :return:
        """
        vacancies_list = []
        for vacancy in vacancies:
            vacancies_list.append(cls(vacancy['name'], vacancy['url'], vacancy['city'], vacancy['salary'],
                                      vacancy['requirement'], vacancy['description']))
        return vacancies_list
