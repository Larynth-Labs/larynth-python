from typing import Literal

NumberCNAMStatus = Literal["failed", "none", "pending", "registered", "unsupported"]

NUMBER_CNAM_STATUS_VALUES: set[NumberCNAMStatus] = {
    "failed",
    "none",
    "pending",
    "registered",
    "unsupported",
}


def check_number_cnam_status(value: str) -> NumberCNAMStatus:
    if value in NUMBER_CNAM_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NUMBER_CNAM_STATUS_VALUES!r}"
    )
