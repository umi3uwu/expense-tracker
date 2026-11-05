# Expense Tracker
## Цель

Это сервис, созданный для подсчета расходов, где пользователь вводит расход с определенными полями, затем этот расход сохраняется в БД, откуда затем можно использовать его для анализа - статистика расходов по промежуткам времени, или поиск по определенным критериям.

## Сущность

- Expense

## Свойства сущности

Expense:
- id
- amount
- date
- category
- source
- note

## Поведение сервиса

- Создать расход
- Редактировать расход
- Удалять расход
- Получать список расходов
- Искать и фильтровать расходы по дате, категории и источнику
- Получать статистику расходов за период (день, неделя, месяц или произвольный период)

## API

- POST /expenses - создать расход
  - Input:
    - amount: int
    - date: date
    - category: str
    - source: str
    - note: str | null, optional
  - Output:
    - id: int
    - amount: int
    - date: date
    - category: str
    - source: str
    - note: str | null

- GET /expenses - получить список расходов и фильтровать
  - Input:
    - category: str, optional
    - source: str, optional
    - date_from: date, optional
    - date_to: date, optional
  - Output:
    - JSON array: [{id, amount, date, category, source, note}]

- PATCH /expenses/{id} - редактировать расход
  - Input:
    - id: int
    - amount: int, optional
    - date: date, optional
    - category: str, optional
    - source: str, optional
    - note: str | null, optional
  - Output:
    - id: int
    - amount: int
    - date: date
    - category: str
    - source: str
    - note: str | null

- DELETE /expenses/{id} - удалить расход
  - Input:
    - id: int
  - Output:
    - deleted: bool
    
- GET /summary - получить статистику расходов
  - Input:
    - period: today | week | month, optional
    - date_from: date, optional
    - date_to: date, optional
  - Output:
    - total_amount: int
    - count: int

## База Данных

Таблица expenses
id amount date        category source    note
1  1000   22.09.2026  Такси    Наличные  Заказ такси для мамы

## Стек

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- Docker