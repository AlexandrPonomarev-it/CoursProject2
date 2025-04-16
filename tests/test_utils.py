import unittest
import pytest
from unittest.mock import patch

from src.utils import (
    filter_vacancies,
    get_vacancies_by_salary,
    sort_vacancies,
    top_vacancies,
    print_vacancies,
    add_result_to_json_file,
)


class TestFilterVacancies(unittest.TestCase):
    def setUp(self):
        self.vacancies_list = [
            {
                "title": "Разработчик Python",
                "description": "Опыт разработки на Python от 3 лет.",
            },
            {
                "title": "Frontend разработчик",
                "description": "Знание HTML, CSS, JavaScript",
            },
            {
                "title": "QA Engineer",
                "description": "Тестирование программного обеспечения",
            },
        ]

    def test_filter_vacancies_with_single_word(self):
        filter_words = ["Python"]
        expected_result = [
            {
                "description": "Опыт разработки на Python от 3 лет.",
                "title": "Разработчик Python",
            },
            {
                "description": "Опыт разработки на Python от 3 лет.",
                "title": "Разработчик Python",
            },
        ]
        actual_result = filter_vacancies(self.vacancies_list, filter_words)
        self.assertEqual(expected_result, actual_result)

    def test_filter_vacancies_with_multiple_words(self):
        filter_words = ["Python", "JavaScript"]
        expected_result = [
            {
                "description": "Опыт разработки на Python от 3 лет.",
                "title": "Разработчик Python",
            },
            {
                "description": "Опыт разработки на Python от 3 лет.",
                "title": "Разработчик Python",
            },
            {
                "description": "Знание HTML, CSS, JavaScript",
                "title": "Frontend разработчик",
            },
        ]
        actual_result = filter_vacancies(self.vacancies_list, filter_words)
        self.assertEqual(expected_result, actual_result)

    def test_filter_vacancies_no_match(self):
        filter_words = ["C++"]
        expected_result = []
        actual_result = filter_vacancies(self.vacancies_list, filter_words)
        self.assertEqual(expected_result, actual_result)

    def test_filter_vacancies_case_insensitive(self):
        filter_words = ["PYTHON"]
        expected_result = [
            {
                "description": "Опыт разработки на Python от 3 лет.",
                "title": "Разработчик Python",
            },
            {
                "description": "Опыт разработки на Python от 3 лет.",
                "title": "Разработчик Python",
            },
        ]
        actual_result = filter_vacancies(self.vacancies_list, filter_words)
        self.assertEqual(expected_result, actual_result)


class TestGetVacanciesBySalary(unittest.TestCase):
    def setUp(self):
        self.vacancy_list = [
            {"title": "Разработчик Python", "salary": {"from": 100000}},
            {"title": "Frontend разработчик", "salary": {"from": 80000}},
            {"title": "QA Engineer", "salary": {"from": 70000}},
        ]

    def test_get_vacancies_above_threshold(self):
        salary = 90000
        expected_result = [
            {"salary": {"from": 80000}, "title": "Frontend разработчик"},
            {"salary": {"from": 70000}, "title": "QA Engineer"},
        ]
        actual_result = get_vacancies_by_salary(self.vacancy_list, salary)
        self.assertEqual(expected_result, actual_result)

    def test_get_vacancies_below_threshold(self):
        salary = 60000
        expected_result = []
        actual_result = get_vacancies_by_salary(self.vacancy_list, salary)
        self.assertEqual(expected_result, actual_result)

    def test_get_vacancies_equal_to_threshold(self):
        salary = 80000
        expected_result = [
            {"salary": {"from": 80000}, "title": "Frontend разработчик"},
            {"salary": {"from": 70000}, "title": "QA Engineer"},
        ]
        actual_result = get_vacancies_by_salary(self.vacancy_list, salary)
        self.assertEqual(expected_result, actual_result)

    def test_empty_vacancy_list(self):
        salary = 50000
        empty_vacancy_list = []
        expected_result = []
        actual_result = get_vacancies_by_salary(empty_vacancy_list, salary)
        self.assertEqual(expected_result, actual_result)


class TestSortVacancies(unittest.TestCase):
    def setUp(self):
        self.range_vacancies = [
            {"title": "Разработчик Python", "salary": {"from": 120000}},
            {"title": "Frontend разработчик", "salary": {"from": 80000}},
            {"title": "QA Engineer", "salary": {"from": 75000}},
            {"title": "Data Scientist", "salary": {"from": 110000}},
            {"title": "Backend разработчик", "salary": {"from": 95000}},
        ]

    def test_sort_vacancies_descending(self):
        expected_result = [
            {"salary": {"from": 120000}, "title": "Разработчик Python"},
            {"salary": {"from": 110000}, "title": "Data Scientist"},
            {"salary": {"from": 95000}, "title": "Backend разработчик"},
            {"salary": {"from": 80000}, "title": "Frontend разработчик"},
            {"salary": {"from": 75000}, "title": "QA Engineer"},
        ]
        actual_result = sort_vacancies(self.range_vacancies)
        self.assertEqual(expected_result, actual_result)

    def test_sort_vacancies_empty_list(self):
        range_vacancies = []
        expected_result = []
        actual_result = sort_vacancies(range_vacancies)
        self.assertEqual(expected_result, actual_result)


class TestTopVacancies(unittest.TestCase):
    def setUp(self):
        self.sorted_vacancy_list = [
            {"title": "Разработчик Python", "salary": {"from": 120000}},
            {"title": "Frontend разработчик", "salary": {"from": 80000}},
            {"title": "QA Engineer", "salary": {"from": 75000}},
            {"title": "Data Scientist", "salary": {"from": 110000}},
            {"title": "Backend разработчик", "salary": {"from": 95000}},
        ]

    def test_top_vacancies(self):
        top_n = 3
        expected_result = [
            {"salary": {"from": 120000}, "title": "Разработчик Python"},
            {"salary": {"from": 80000}, "title": "Frontend разработчик"},
            {"salary": {"from": 75000}, "title": "QA Engineer"},
        ]
        actual_result = top_vacancies(self.sorted_vacancy_list, top_n)
        self.assertEqual(expected_result, actual_result)

    def test_top_vacancies_all(self):
        top_n = 10
        expected_result = self.sorted_vacancy_list
        actual_result = top_vacancies(self.sorted_vacancy_list, top_n)
        self.assertEqual(expected_result, actual_result)

    def test_top_vacancies_zero(self):
        top_n = 0
        expected_result = []
        actual_result = top_vacancies(self.sorted_vacancy_list, top_n)
        self.assertEqual(expected_result, actual_result)

    def test_top_vacancies_negative(self):
        top_n = -1
        expected_result = []
        actual_result = top_vacancies(self.sorted_vacancy_list, top_n)
        self.assertEqual(expected_result, actual_result)


class TestPrintVacancies(unittest.TestCase):
    @patch("builtins.print")
    def test_print_vacancies_with_data(self, mock_print):
        # Тестовые данные
        vacancies = [
            {
                "ID": 1,
                "name": "Engineer",
                "salary": {"from": 50000},
                "url": "http://example.com",
                "snippet": {"responsibility": "Engineering stuff"},
            },
            {
                "ID": 2,
                "name": "Developer",
                "salary": {"from": 60000},
                "url": "http://example.com/dev",
                "snippet": {"responsibility": "Developing stuff"},
            },
        ]

        # Вызов функции
        print_vacancies(vacancies)

        # Проверка вывода
        calls = [
            unittest.mock.call(
                f"ID вакансии: 1\n"
                f"Профессия: Engineer\n"
                f"Зарплата от: 50000\n"
                f"URL: http://example.com\n"
                f"Описание профессии: Engineering stuff"
            ),
            unittest.mock.call(
                f"ID вакансии: 2\n"
                f"Профессия: Developer\n"
                f"Зарплата от: 60000\n"
                f"URL: http://example.com/dev\n"
                f"Описание профессии: Developing stuff"
            ),
        ]
        mock_print.assert_has_calls(calls, any_order=True)

    @patch("builtins.print")
    def test_print_vacancies_empty_list(self, mock_print):
        # Вызов функции с пустым списком
        print_vacancies([])

        # Проверка вывода
        mock_print.assert_called_once_with("Вакансий по заданным параметрам не найдено")


if __name__ == "__main__":
    unittest.main()
