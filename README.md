# API Testing Practice

Учебный проект для практики HTTP, REST API и API-автотестов на Python.

Проект использует `requests`, `pytest`, `jsonschema` и менеджер зависимостей `uv`.

## Что изучается

- HTTP request / response
- REST-методы `GET`, `POST`, `PUT`, `PATCH`, `DELETE`
- status code
- JSON body
- headers и `Content-Type`
- query params
- negative API cases
- schema validation через `jsonschema`
- автотесты API через `pytest`
- управление зависимостями через `uv`, `pyproject.toml` и `uv.lock`
- автоматический запуск тестов через GitHub Actions

## Учебный API

Используется публичный сервис:

```text
https://jsonplaceholder.typicode.com
```

Важно: это учебный fake API. `POST`, `PUT`, `PATCH`, `DELETE` возвращают успешные ответы, но реально данные на сервере не сохраняются.

## Структура проекта

```text
api-testing-practice/
├── .github/workflows/tests.yml
├── tests/
│   └── test_posts_api.py
├── api_client.py
├── pyproject.toml
├── uv.lock
├── pytest.ini
└── README.md
```

## Установка зависимостей

```bash
uv sync
```

## Запуск демонстрационного скрипта

```bash
uv run python api_client.py
```

## Запуск тестов

```bash
uv run pytest
```

## Что покрыто тестами

- `GET /posts/1` — получение одного поста
- `GET /posts` — получение списка постов
- `GET /posts/999999` — проверка `404 Not Found`
- `POST /posts` — создание поста
- `PUT /posts/1` — полное обновление поста
- `PATCH /posts/1` — частичное обновление поста
- `DELETE /posts/1` — удаление поста
- `GET /posts?userId=1` — фильтрация через query params
- `GET /posts?userId=999999` — пустой результат фильтрации
- проверка `Content-Type`
- negative cases для неполного JSON body
- schema validation для одного поста и списка постов

## Что показывает проект

Проект демонстрирует базовые навыки API automation:

- отправка HTTP-запросов через `requests`
- проверка `status_code`
- чтение JSON-ответа через `response.json()`
- проверка обязательных полей ответа
- проверка типов данных
- проверка позитивных и негативных сценариев
- параметризация API-тестов
- проверка JSON-структуры через `jsonschema`
- запуск тестов локально через `uv`
- запуск тестов в CI через GitHub Actions