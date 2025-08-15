from src.masks import get_mask_card_number, get_mask_account
from datetime import datetime

def mask_account_card(info: str) -> str:
    """
    Обрабатывает строку с информацией о карте или счете
    и возвращает маскированную строку.
    """
    parts = info.strip().split()
    if not parts:
        return info  # если строка пустая или некорректная

    # Определяем тип по первому слову
    card_types = {"Visa", "Maestro", "MasterCard", "Visa Classic", "Visa Gold", "Visa Platinum"}

    first_word = parts[0]

    if first_word == "Счет":
        # Обработка счета
        account_number = parts[1]
        masked_account = get_mask_account(account_number)
        return f"Счет {masked_account}"

    elif first_word in card_types:
        # Обработка карты
        # Остальные части — название карты
        card_name_parts = parts[:-1]
        card_number = parts[-1]
        masked_card_number = get_mask_card_number(card_number)
        return " ".join(card_name_parts) + " " + masked_card_number

    else:
        # Неизвестный формат, возвращаем исходную строку
        return info


def get_date(date_str: str) -> str:
    """
    Преобразует строку с датой из формата ISO 8601 ("2024-03-11T02:26:18.671407")
    в формат "ДД.ММ.ГГГГ".
    """
    try:
        dt = datetime.fromisoformat(date_str)
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        # В случае некорректного формата возвращаем исходную строку или пустую
        return date_str
