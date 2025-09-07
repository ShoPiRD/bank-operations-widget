from typing import Optional, Union


def get_mask_card_number(card: Optional[Union[str, int]]) -> str:
    """Функция get_mask_card_number принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX, где X — это цифра номера.
     То есть видны первые 6 цифр и последние 4 цифры, остальные символы отображаются звездочками,
    номер разбит по блокам по 4 цифры, разделенным пробелами."""
    # приводим card к строковому типу
    card_str = str(card)
    # длина номера карты
    n = len(card_str)
    # первые 6 и последние 4 цифры оставляем видимыми
    visible_indices = set(range(6)) | set(range(n - 4, n))
    # Новая строка с масками
    masked = "".join(ch if i in visible_indices else "*" for i, ch in enumerate(card_str))
    #  разбиваем на части по 4 символа
    blocks = [masked[i : i + 4] for i in range(0, n, 4)]
    return " ".join(blocks)


def get_mask_account(account_number: Union[str, int]) -> str:
    """Функция get_mask_account принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX, где X — это цифра номера.
    То есть видны только последние 4 цифры номера, а перед ними — две звездочки."""
    account_str = str(account_number)
    last_four_nums = account_str[-4:]
    return "**" + last_four_nums
