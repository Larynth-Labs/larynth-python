from typing import Literal

UsageRowUnit = Literal["brand_month", "call", "minute", "number_month"]

USAGE_ROW_UNIT_VALUES: set[UsageRowUnit] = {
    "brand_month",
    "call",
    "minute",
    "number_month",
}


def check_usage_row_unit(value: str) -> UsageRowUnit:
    if value in USAGE_ROW_UNIT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {USAGE_ROW_UNIT_VALUES!r}"
    )
