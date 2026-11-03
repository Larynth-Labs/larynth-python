from typing import Literal

CallReceiptRounding = Literal["started_minute"]

CALL_RECEIPT_ROUNDING_VALUES: set[CallReceiptRounding] = {
    "started_minute",
}


def check_call_receipt_rounding(value: str) -> CallReceiptRounding:
    if value in CALL_RECEIPT_ROUNDING_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_RECEIPT_ROUNDING_VALUES!r}"
    )
