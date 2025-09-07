import pytest
from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Visa Classic 1234567812345678", "Visa Classic 1234 56** **** 5678"),
        ("Maestro 1234567890123456", "Maestro 1234 56** **** 3456"),
    ],
)
def test_mask_account_card_valid(input_str: str, expected: str) -> None:
    result = mask_account_card(input_str)
    assert result == expected


def test_mask_account_card_empty_string() -> None:
    assert mask_account_card("") == ""


def test_mask_account_card_only_spaces() -> None:
    assert mask_account_card("   ") == "   "


def test_mask_account_card_unknown_format() -> None:
    input_str = "UnknownType 1234567890"
    assert mask_account_card(input_str) == input_str


def test_mask_account_card_missing_number() -> None:
    assert mask_account_card("Счет") == "Счет"


def test_mask_account_card_no_parts() -> None:
    assert mask_account_card(" ") == " "


@pytest.mark.parametrize(
    "input_date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-01T00:00:00", "01.12.2023"),
        ("2022-01-31T23:59:59", "31.01.2022"),
    ],
)
def test_get_date_valid(input_date: str, expected: str) -> None:
    assert get_date(input_date) == expected


@pytest.mark.parametrize(
    "input_date",
    [
        "",
        "not-a-date",
        "2024-13-01T00:00:00",
        "2024-02-30T00:00:00",
    ],
)
def test_get_date_invalid(input_date: str) -> None:
    assert get_date(input_date) == input_date
