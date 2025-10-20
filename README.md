# Sprint_7 Автотесты API


В проекте зайдествованы автотесты для проверки сервиса Яндекс.Самокат с помощью Requests, Pytest и Allure.

## Установка и запуск

Установка зависимостей:

`pip install -r requirements.txt`

Запуск тестов:

`pytest -v`


Запуск автотестов и создание отчета о тестировании в Allure:

`pytest --alluredir=allure_results`

Показ отчета из результатов тестов:

`allure serve ./allure_results`

Генерация отчета из результатов тестов:

`allure generate ./allure_results/ -o allure_report `


## Структура проекта

- Sprint_7/
  - allure_report/ # сгенерированный отчет
  - allure_results/ # сгенерированные файлы до отчета
  - data/ # данные для использования в тестах
  - locators/ # свойства поиска элементов для разных страниц
  - helpers/ # классы c действиями для разных ручек
  - tests/  # Тесты, сгруппированные по функционалу
  - conftest.py # Фикстуры Pytest
  - pytest.ini # настройки pytest 
  - README.md # Текущий файл
  - requirements.txt # Зависимости проекта

  

Автор: Нестер Екатерина Васильевна
30-31 когорта
https://github.com/EkaterinaNester89/