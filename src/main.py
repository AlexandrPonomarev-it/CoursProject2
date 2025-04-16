
from src.get_hh_vacancy import GetHHVacancies
from src.utils import filter_vacancies, get_vacancies_by_salary, sort_vacancies, top_vacancies, print_vacancies, \
    add_result_to_json_file
from src.vacancy import Vacancy

# Экземпляр класса открытия вакансии с hh.ru
hh_api = GetHHVacancies()

search_query = input("Введите поисковый запрос: ")

# Получение вакансий с hh.ru в формате списка словарей
hh_vacancies = hh_api.load_vacancies(search_query)

# Запись данных в формате класса вакансий
vacancy = Vacancy.add_vacancy_to_list(hh_vacancies)

#Удаление информации о вакансиях из файла
# json_saver = ProcessingVacancies(vacancy, "r")
# json_saver.del_vacancies()


def user_interaction():
    """ Функция для взаимодействия с пользователем"""

    # Данные от пользователя для получения вакансий
    top_n = int
    salary_range = int

    while type(top_n) is not int:
        top = input("Введите число, для указания топ вакансий: ")
        if top.isdigit():
            top_n = int(top)

    inp_filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

    while type(salary_range) is not int:
        salary = input("Введите минимальную зарплату: ")
        if salary.isdigit():
            salary_range = int(salary)


    filtered_vacancies = filter_vacancies(vacancy, inp_filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)

    top_list_vacancies = top_vacancies(sorted_vacancies, top_n)

    print_vacancies(top_list_vacancies)

    return top_list_vacancies



if __name__ == "__main__":
    ready_list_vacancy = user_interaction()
    add_result_to_json_file(ready_list_vacancy)

