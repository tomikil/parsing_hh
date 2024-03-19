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
