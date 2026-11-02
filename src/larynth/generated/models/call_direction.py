from typing import Literal

CallDirection = Literal["inbound", "outbound", "web_test"]

CALL_DIRECTION_VALUES: set[CallDirection] = {
    "inbound",
    "outbound",
    "web_test",
}


def check_call_direction(value: str) -> CallDirection:
    if value in CALL_DIRECTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_DIRECTION_VALUES!r}"
    )
