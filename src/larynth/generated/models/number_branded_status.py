from typing import Literal

NumberBrandedStatus = Literal["active", "failed", "none", "pending", "unsupported"]

NUMBER_BRANDED_STATUS_VALUES: set[NumberBrandedStatus] = {
    "active",
    "failed",
    "none",
    "pending",
    "unsupported",
}


def check_number_branded_status(value: str) -> NumberBrandedStatus:
    if value in NUMBER_BRANDED_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NUMBER_BRANDED_STATUS_VALUES!r}"
    )
