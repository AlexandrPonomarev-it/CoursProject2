from abc import ABC, abstractmethod

import requests


class Parser(ABC):
    """Базовый класс для работы с API подключением к HH"""

    def __init__(self, *args, **kwargs) -> None:
        """Конструктор для создания экземпляров класса Parser"""
        super().__init__()

    @abstractmethod
    def load_vacancies(self, keyword):
        """Абстрактный метод для получения инвормации о вакансиях с HH"""
        pass


class GetHHVacancies(Parser, ABC):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        """Конструктор для создания экземпляра класса GetHHVacancies"""
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = []
        super().__init__()

    def __connect_to_api_status(self):
        """Проверка соединения с адресом HH"""
        try:
            response = requests.get(self.__url)
            response.raise_for_status()
            return True
        except ConnectionError as e:
            print(f"Ошибка подключения: {e}")
            return False

    def load_vacancies(self, keyword):
        """Загрузка вакансий по ключевому слову с сайта HH"""
        if not self.__connect_to_api_status():
            return []
        self.__params["text"] = keyword

        while self.__params.get("page") != 3:
            try:
                response = requests.get(
                    self.__url, headers=self.__headers, params=self.__params
                )
                vacancies = response.json()["items"]
                self.__vacancies.extend(vacancies)
                self.__params["page"] += 1
            except ConnectionError as e:
                print(f"Ошибка при загрузке вакансий: {e}")

        return self.__vacancies
