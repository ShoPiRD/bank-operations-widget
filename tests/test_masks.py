import pytest
from typing import Optional

from src.masks import get_mask_card_number


@pytest.mark.parametrize(
    "input_card, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("1234 5678 1234 5678", "1234 56** **** 5678"),
        ("12345678", "1234 56**"),
        ("", ""),
        (None, ""),
    ],
)
def test_get_mask_card_number(input_card: Optional[str], expected: str) -> None:
    input_val = input_card if input_card is not None else ""
    assert get_mask_card_number(input_val) == expected
