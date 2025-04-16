import unittest
from unittest.mock import patch, MagicMock

from src.get_hh_vacancy import GetHHVacancies


class TestLoadVacancies(unittest.TestCase):
    def setUp(self):
        """Настройка объектов для тестирования."""
        self.hh_vacancies = GetHHVacancies()

    @patch('requests.get')
    def test_load_vacancies_success(self, mock_get):
        """Тестируем успешную загрузку вакансий."""
        # Подготовка мока для ответа от API
        mock_get.return_value.ok = True
        mock_get.return_value.json = MagicMock(side_effect=[
            {'items': [{'id': 1, 'title': 'Developer'}]},
            {'items': [{'id': 2, 'title': 'Developer'}]},
            {'items': []}  # После трех страниц ожидаем пустой ответ для остановки цикла
        ])

        result = self.hh_vacancies.load_vacancies('developer')

        # Проверяем, были ли добавлены две вакансии
        self.assertEqual(len(result), 2)


    @patch('requests.get')
    def test_load_vacancies_connection_error(self, mock_get):
        """Тестируем обработку ошибок подключения."""
        # Имитация ошибки подключения
        mock_get.side_effect = ConnectionError("Failed to connect")

        result = self.hh_vacancies.load_vacancies('developer')

        # Проверяем, что в результате пустой список
        self.assertEqual(result, [])
        # Убеждаемся, что была обработана ошибка
        mock_get.assert_called_once()


if __name__ == '__main__':
    unittest.main()
