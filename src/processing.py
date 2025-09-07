
from typing import List, Dict
from datetime import datetime

def sort_by_date(transactions: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список транзакций по дате.
    :param transactions: список словарей с транзакциями
    :param reverse: сортировать по убыванию (по умолчанию True)
    :return: отсортированный список транзакций
    """
    def parse_date(transaction: Dict) -> datetime:
        date_str = transaction.get('date', '')
        # Преобразуем строку в datetime, если формат ISO 8601
        try:
            return datetime.fromisoformat(date_str)
        except ValueError:
            # Если дата отсутствует или неверный формат, возвращаем минимальное значение
            return datetime.min

    return sorted(transactions, key=parse_date, reverse=reverse)
