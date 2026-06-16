# API Testing Practice

Учебный проект для изучения HTTP, API и автотестов API на Python.

## Что изучаем

- HTTP-запросы
- HTTP-ответы
- status code
- JSON body
- библиотеку `requests`
- API-тесты через `pytest`
- базовые REST-методы: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`
- query params
- headers
- проверку `Content-Type`
- GitHub Actions для автоматического запуска тестов

## Учебный API

Используется публичный API:

```text
https://jsonplaceholder.typicode.com
```

## Установка зависимостей

```bash
python -m pip install -r requirements.txt
```

## Запуск первого скрипта

```bash
python api_client.py
```

## Запуск тестов

```bash
python -m pytest
```

## Что покрыто тестами

- `GET /posts/1` — получение одного поста
- `GET /posts` — получение списка постов
- `GET /posts/999999` — проверка ответа `404 Not Found`
- `POST /posts` — создание поста
- `PUT /posts/1` — полное обновление поста
- `PATCH /posts/1` — частичное обновление поста
- `DELETE /posts/1` — удаление поста
- `GET /posts?userId=1` — фильтрация через query params
- `GET /posts?userId=999999` — пустой результат фильтрации
- проверка заголовка ответа `Content-Type`

## Что показывает проект

Проект демонстрирует базовые навыки API automation:

- отправку HTTP-запросов через `requests`;
- проверку `status_code`;
- чтение JSON-ответа через `response.json()`;
- проверку обязательных полей ответа;
- проверку типов данных;
- проверку успешных и ошибочных сценариев;
- проверку query params;
- проверку headers и `Content-Type`;
- запуск API-тестов через `pytest`;
- автоматический запуск тестов через GitHub Actions.
