# Expense Tracker

Простой API для учета расходов.

Можно добавлять расходы, изменять и удалять их, фильтровать по дате, категории и источнику, а также смотреть статистику за определенный период.

## Стек

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Docker

## Запуск локально

Установить зависимости:

```bash
pip install -r requirements.txt
```

Запустить сервер:

```bash
uvicorn app.main:app --reload
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

## Запуск через Docker

```bash
docker compose up --build -d
```

Swagger:

```text
http://localhost:8001/docs
```

Остановить контейнер:

```bash
docker compose stop
```

## API

- `POST /expenses` - добавить расход
- `GET /expenses` - получить расходы и фильтровать их
- `PATCH /expenses/{id}` - изменить расход
- `DELETE /expenses/{id}` - удалить расход
- `GET /summary` - получить статистику расходов

Для `/summary` можно использовать:

```text
?period=today
?period=week
?period=month
```

Также можно указать свой период:

```text
?date_from=2026-11-01&date_to=2026-11-12
```

Данные сохраняются в SQLite базе.
