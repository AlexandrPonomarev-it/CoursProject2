
class Vacancy:

    __slots__ = ['vac_id', 'name', 'salary', 'requirement', 'vacancy_url']

    def __init__(self, vac_id, name, salary, requirement, vacancy_url):
        """ Конструктор для создания экземпляров класса Vacancy"""
        self.vac_id = vac_id
        self.name = name
        self.__valid_salary(salary)
        self.requirement = requirement
        self.vacancy_url = vacancy_url

    def vacancy_dict(self):
        """ Преобразует объекты класса в словарь """
        return {
            "ID": self.vac_id,
            "name": self.name,
            "salary": self.salary,
            "requirement": self.requirement,
            "vacancy_url": self.vacancy_url
        }

    def __valid_salary(self, salary):
        """ Валидация данных по зарплате (есть данные о зарплате или они отсутствуют """
        if type(salary) == int:
            self.salary = salary
        else:
            self.salary = 0

    def __le__(self, other):
        """ Сравнение зарплаты меньше или равно """
        if self.salary > 0 and other.salary > 0:
            if not isinstance(other, Vacancy):
                return NotImplemented
            return self.salary <= other.salary
        else:
            return "Зарплата не указана"

    def __ge__(self, other):
        """ Сравнение зарплаты больше или равно """
        if self.salary > 0 and other.salary > 0:
            if not isinstance(other, Vacancy):
                return NotImplemented
            return self.salary >= other.salary
        else:
            return "Зарплата не указана"

    @staticmethod
    def add_vacancy_to_list(list_vac):
        """ Вывод вакансии по указанным параметрам """
        list_class_vacancy = []
        for vac in list_vac:
            if type(vac["salary"]) == dict:
                list_class_vacancy.append({
                    "ID": vac["id"],
                    "name": vac["name"],
                    "salary": vac["salary"],
                    "snippet": vac["snippet"],
                    "url": vac["url"]
                })
        return list_class_vacancy
