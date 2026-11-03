from typing import Literal

ListNumbersStatus = Literal[
    "active", "failed", "ordering", "released", "releasing", "suspended", "verifying"
]

LIST_NUMBERS_STATUS_VALUES: set[ListNumbersStatus] = {
    "active",
    "failed",
    "ordering",
    "released",
    "releasing",
    "suspended",
    "verifying",
}


def check_list_numbers_status(value: str) -> ListNumbersStatus:
    if value in LIST_NUMBERS_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_NUMBERS_STATUS_VALUES!r}"
    )
