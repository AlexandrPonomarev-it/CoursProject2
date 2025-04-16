import pytest

from src.vacancy import Vacancy


@pytest.fixture
def first_vacancy():
    return Vacancy(
        vac_id=1,
        name="Разработчик",
        salary=100000,
        requirement="Работа разработчиком",
        vacancy_url="https://api.hh.ru/vacancies/1?host=hh.ru",
    )


@pytest.fixture
def second_vacancy():
    return Vacancy(
        vac_id=2,
        name="Тестировщик",
        salary="90000",
        requirement="Работа тестировщиком",
        vacancy_url="https://api.hh.ru/vacancies/2?host=hh.ru",
    )


@pytest.fixture
def third_vacancy():
    return Vacancy(
        vac_id=3,
        name="Фронт-разработчик",
        salary=90000,
        requirement="Работа Фронт-разработчиком",
        vacancy_url="https://api.hh.ru/vacancies/3?host=hh.ru",
    )


@pytest.fixture
def vac_list():
    return {
        "ID": 1,
        "name": "Разработчик",
        "salary": 100000,
        "snippet": "Работа разработчиком",
        "url": "https://api.hh.ru/vacancies/1?host=hh.ru",
    }
