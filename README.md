# Программа для поиска вакансий с HH.ru


## В программе реализованы возможности поиска информации о вакансиях по запросу пользователя


# Все встроенные модули интегрированы в файл main.py, который реализует поиск вакансий и выводит топ по указанному количеству вакансий с учетом введенной пользователем зарплаты

1. **Клонируйте репозиторий:**
        git@github.com:AlexandrPonomarev-it/CoursProject2.git

2. **Создайте виртуальное окружение и активируйте его:**
    ```sh
    python -m venv venv
    venv\Scripts\activate
    ```
## Тестирование:
### для запуска теста выполните команду: pytest --cov
### Список зависимостей:
[tool.poetry.dependencies]
python = "^3.13"
requests = "^2.32.3"
python-dotenv = "^1.0.1"
pandas = "^2.2.3"
openpyxl = "^3.1.5"


[tool.poetry.group.lint.dependencies]
black = "^24.10.0"
flake8 = "^7.1.1"
mypy = "^1.13.0"
isort = "^5.13.2"


[tool.poetry.group.dev.dependencies]
pytest = "^8.3.4"
pytest-cov = "^6.0.0"

### Запуск проекта:

Для запуска проекта выполните:
```sh
 python manage.py runserver    
```

### Команда проекта: AlexandrPonomarev-it

### Источники: Виртуальная школа SKYPRO