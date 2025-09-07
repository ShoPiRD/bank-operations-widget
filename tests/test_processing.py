from typing import List, Dict
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default() -> None:
    data: List[Dict] = [
        {'id': 1, 'state': 'EXECUTED'},
        {'id': 2, 'state': 'CANCELED'},
        {'id': 3, 'state': 'EXECUTED'}
    ]
    result = filter_by_state(data)
    assert all(tx['state'] == 'EXECUTED' for tx in result)
    assert len(result) == 2


def test_filter_by_state_custom() -> None:
    data: List[Dict] = [
        {'id': 1, 'state': 'EXECUTED'},
        {'id': 2, 'state': 'CANCELED'},
        {'id': 3, 'state': 'EXECUTED'}
    ]
    result = filter_by_state(data, state='CANCELED')
    assert all(tx['state'] == 'CANCELED' for tx in result)
    assert len(result) == 1


def test_sort_by_date_default() -> None:
    data: List[Dict] = [
        {'id': 1, 'date': '2020-01-01T10:00:00'},
        {'id': 2, 'date': '2021-01-01T10:00:00'},
        {'id': 3, 'date': '2019-01-01T10:00:00'}
    ]
    result = sort_by_date(data)
    dates = [tx['date'] for tx in result]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_ascending() -> None:
    data: List[Dict] = [
        {'id': 1, 'date': '2020-01-01T10:00:00'},
        {'id': 2, 'date': '2021-01-01T10:00:00'},
        {'id': 3, 'date': '2019-01-01T10:00:00'}
    ]
    result = sort_by_date(data, reverse=False)
    dates = [tx['date'] for tx in result]
    assert dates == sorted(dates, reverse=False)