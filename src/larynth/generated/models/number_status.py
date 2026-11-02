from typing import Literal

NumberStatus = Literal[
    "active", "failed", "ordering", "released", "releasing", "suspended"
]

NUMBER_STATUS_VALUES: set[NumberStatus] = {
    "active",
    "failed",
    "ordering",
    "released",
    "releasing",
    "suspended",
}


def check_number_status(value: str) -> NumberStatus:
    if value in NUMBER_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NUMBER_STATUS_VALUES!r}"
    )
