
# Bank Operations Widget

Проект содержит функции для фильтрации и сортировки банковских операций.

## Функции

- `filter_by_state(transactions, state='EXECUTED')` — фильтрует операции по статусу.
- `sort_by_date(transactions, reverse=True)` — сортирует операции по дате.

  Для сортировки используется стандартный модуль Python `datetime`.  
  Даты должны быть в формате ISO 8601 (например, `"2019-07-03T18:35:29.512364"`).  
  Если дата отсутствует или имеет неверный формат, такая операция помещается в конец отсортированного списка.

## Пример использования

```python
from src.processing import filter_by_state, sort_by_date

transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Фильтрация по состоянию 'EXECUTED'
executed_transactions = filter_by_state(transactions)

# Сортировка по дате (по убыванию)
sorted_transactions = sort_by_date(executed_transactions)

print(sorted_transactions)