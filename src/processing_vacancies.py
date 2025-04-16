import json
from abc import ABC, abstractmethod


class BaseProcessingVacancies(ABC):

    def __init__(self, *args, **kwargs) -> None:
        """Конструктор для создания экземпляров класса BaseProcessingVacancies"""
        super().__init__()

    @abstractmethod
    def read_vacancies(self):
        pass

    @abstractmethod
    def add_vacancies(self, file_worker):
        pass

    @abstractmethod
    def del_vacancies(self):
        pass


class ProcessingVacancies(BaseProcessingVacancies):
    """Класс для обработки вакансий"""

    def __init__(self, mode="a+", file_name="../src/vacancies.json"):
        """Конструктор для создания экземпляров класса ProcessingVacancies"""
        self.mode = mode
        self.file_name = file_name
        super().__init__()

    def read_vacancies(self):
        """Чтение данных их файла json"""
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                data = json.load(file)
            if data:
                return data
            else:
                return False
        except FileNotFoundError:
            return False
        except json.JSONDecodeError:
            return False

    def add_vacancies(self, file_worker):
        """Запись данных в файл json"""
        with open(self.file_name, "w", encoding="utf-8") as file:
            file.write(json.dumps(file_worker, indent=4, ensure_ascii=False))

    def del_vacancies(self):
        """Удаление данных из файла"""
        with open(self.file_name, "w"):
            pass
