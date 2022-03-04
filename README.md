### welbex
---

check https://welbex-lev.herokuapp.com/ 

---

if you want to run local:
1. pip install -r requirements.txt
2. change .env file
3. python manage.py migrate
4. change index.js fetch domain to 127.0.0.1:8000

---

# ТЗ
# **Тестовое задание web-программист (Python)**

Нужно разработать таблицу в формате Single Page Application.

**Требования к таблице.**

1. Таблица должна содержать 4 колонки:
    1. Дата
    2. Название
    3. Количество
    4. Расстояние
2. База данных может быть mySQL/PostgreSQL
3. Таблица должна иметь сортировку по всем полям кроме даты. Фильтрация должна быть в виде двух выпадающих списков и текстового поля:
    1. Выбор колонки, по которой будет фильтрация
    2. Выбор условия (равно, содержит, больше, меньше)
    3. Поле для ввода значения для фильтрации
4. Таблица должна содержать пагинацию

Вся таблица должна работать без перезагрузки страницы.
