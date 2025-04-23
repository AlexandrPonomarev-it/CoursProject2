from src.processing_vacancies import ProcessingVacancies


def filter_vacancies(vacancies_list: list, filter_words: list) -> list:
    """Функция для отбора вакансии по ключевому слову на сайте hh.ru"""
    new_vacancy_list = []
    for vacancy in vacancies_list:
        for value in vacancy.values():
            if type(value) is str:
                for words in filter_words:
                    if words.lower() in value.lower():
                        new_vacancy_list.append(vacancy)
                    elif type(value) is dict:
                        if words.lower() in value["requirement"].lower() or words in value["responsibility"].lower():
                            new_vacancy_list.append(vacancy)
                        else:
                            continue
                    else:
                        continue
            else:
                continue
    return new_vacancy_list


def get_vacancies_by_salary(vacancy_list: list, salary: int) -> list:
    """Фильтрация списка вакансий по зарплате"""
    ranged_vacancies_list = []
    for vacancy in vacancy_list:
        for key, value in vacancy.items():
            if key == "salary":
                if type(value["from"]) is int and salary >= value["from"]:
                    ranged_vacancies_list.append(vacancy)
                else:
                    continue
    return ranged_vacancies_list


def sort_vacancies(range_vacancies: list) -> list:
    """Сортировка вакансий по зарплате"""
    vacancies_sort = sorted(range_vacancies, key=lambda salary: salary["salary"]["from"], reverse=True)
    return vacancies_sort


def top_vacancies(sorted_vacancy_list: list, top_n: int) -> list:
    """Список заданного топа вакансий"""
    top_vacancy_list = []
    for vacancy in sorted_vacancy_list:
        if len(top_vacancy_list) < top_n:
            top_vacancy_list.append(vacancy)
    return top_vacancy_list


def print_vacancies(sorted_top_vac_list: list) -> None:
    """Вывод списка отобранных вакансий"""
    if sorted_top_vac_list:
        for vac in sorted_top_vac_list:
            print(
                f"ID вакансии: {vac['ID']}\n"
                f"Профессия: {vac["name"]}\n"
                f"Зарплата от: {vac["salary"]["from"]}\n"
                f"URL: {vac["url"]}\n"
                f"Описание профессии: {vac["snippet"]["responsibility"]}"
            )
    else:
        print("Вакансий по заданным параметрам не найдено")


def add_result_to_json_file(data: list) -> None:
    """Добавление списка в файл json"""
    ex_class_vac = ProcessingVacancies()
    list_vac = ex_class_vac.read_vacancies()
    unic_list = []
    if list_vac is False:
        ex_class_vac.add_vacancies(data)
    else:
        list_vac.extend(data)
        for vac in list_vac:
            if vac not in unic_list:
                unic_list.append(vac)
                ex_class_vac.add_vacancies(unic_list)
