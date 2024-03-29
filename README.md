[![GitHub](https://img.shields.io/badge/GitHub-Kirill--Svitsov-blue)](https://github.com/Kirill-Svitsov)
# Visual

## Description
Тестовое задание для Visual.
Задача: Реализация простого API для управления пользователями
Описание:
Требуется создать простой веб-сервис для управления пользователями. Сервис должен предоставлять API для создания, просмотра и удаления пользователей.
Требования:
1. Модель пользователя:
   - Имя (строка, до 50 символов);
   - Электронная почта (строка, уникальная);
   - Дата регистрации.
2. Операции:
   - Создание нового пользователя (при создании устанавливать текущую дату регистрации);
   - Получение списка всех пользователей;
   - Получение информации о конкретном пользователе по его идентификатору;
   - Удаление пользователя.
3. Технологии:
   - Язык программирования: Python
Дополнительные пояснения:
- Важно обеспечить защиту API от некорректных запросов и некорректных данных.
- Предполагается, что проект будет развернут локально, поэтому включите инструкции по установке и запуску.

## Technologies

- Python 3.12
- Django 4.2.7
- Django Rest Framework
- SQL

## Launching the Project in Development Mode

- Создать и активировать виртуальное окружение.
- Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

В папке, содержащей manage.py, выполнить команды:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py runserver
```
Для проекта доступна документация по адресу:
```
http://127.0.0.1:8000/schema/redoc/
```
Для тестирования лучше всего подходит постман, поэтому прежде необходимо создать пользователя
согласно документации и получить токен.
