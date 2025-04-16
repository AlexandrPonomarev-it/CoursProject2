import unittest
from src.processing_vacancies import ProcessingVacancies


class TestProcessingVacancies(unittest.TestCase):

    def setUp(self):
        # Создаем временный файл для тестирования
        self.temp_file = "test_vacancies.json"
        self.vacancy_data = [
            {"title": "Python Developer", "salary": 100000},
            {"title": "Java Developer", "salary": 120000},
        ]

        # Создаем объект класса для тестирования
        self.processor = ProcessingVacancies(mode="w+", file_name=self.temp_file)

    def tearDown(self):
        # Удаляем временный файл после завершения тестов
        import os

        os.remove(self.temp_file)

    def test_read_vacancies(self):
        # Проверка метода read_vacancies при наличии данных
        self.processor.add_vacancies(self.vacancy_data)
        result = self.processor.read_vacancies()
        self.assertEqual(result, self.vacancy_data)

    def test_add_vacancies(self):
        # Проверка метода add_vacancies
        self.processor.add_vacancies(self.vacancy_data)
        result = self.processor.read_vacancies()
        self.assertEqual(result, self.vacancy_data)

    def test_del_vacancies(self):
        # Проверка метода del_vacancies
        self.processor.del_vacancies()
        result = self.processor.read_vacancies()
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
