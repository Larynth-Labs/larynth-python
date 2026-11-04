from typing import Literal

NumberStatus = Literal[
    "active", "failed", "ordering", "released", "releasing", "suspended", "verifying"
]

NUMBER_STATUS_VALUES: set[NumberStatus] = {
    "active",
    "failed",
    "ordering",
    "released",
    "releasing",
    "suspended",
    "verifying",
}


def check_number_status(value: str) -> NumberStatus:
    if value in NUMBER_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NUMBER_STATUS_VALUES!r}"
    )
