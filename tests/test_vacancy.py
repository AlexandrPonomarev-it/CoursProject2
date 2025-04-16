from src.vacancy import Vacancy


def test_vacancy(first_vacancy):
    assert first_vacancy.vac_id == 1
    assert first_vacancy.name == "Разработчик"
    assert first_vacancy.salary == 100000
    assert first_vacancy.requirement == "Работа разработчиком"
    assert first_vacancy.vacancy_url == "https://api.hh.ru/vacancies/1?host=hh.ru"


def test_valid_salary(first_vacancy, third_vacancy, second_vacancy):
    assert second_vacancy.salary == 0
    assert first_vacancy.salary >= third_vacancy.salary


def test_add_vacancy_to_list():
    # Тестовые данные
    list_vac = [
        {
            "id": 1,
            "name": "Junior Developer",
            "salary": {"from": 50000, "to": 70000},
            "snippet": "Description of the job.",
            "url": "https://example.com/jobs/1",
        },
        {
            "id": 2,
            "name": "Senior Developer",
            "salary": 80000,
            "snippet": "Another description.",
            "url": "https://example.com/jobs/2",
        },
    ]

    expected_result = [
        {
            "ID": 1,
            "name": "Junior Developer",
            "salary": {"from": 50000, "to": 70000},
            "snippet": "Description of the job.",
            "url": "https://example.com/jobs/1",
        }
    ]

    result = Vacancy.add_vacancy_to_list(list_vac)

    assert result == expected_result, result
