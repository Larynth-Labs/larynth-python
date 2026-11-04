from typing import Literal

CallTransferMode = Literal["cold", "warm"]

CALL_TRANSFER_MODE_VALUES: set[CallTransferMode] = {
    "cold",
    "warm",
}


def check_call_transfer_mode(value: str) -> CallTransferMode:
    if value in CALL_TRANSFER_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_TRANSFER_MODE_VALUES!r}"
    )
