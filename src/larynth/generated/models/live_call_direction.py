from typing import Literal

LiveCallDirection = Literal["inbound", "outbound", "web_test"]

LIVE_CALL_DIRECTION_VALUES: set[LiveCallDirection] = {
    "inbound",
    "outbound",
    "web_test",
}


def check_live_call_direction(value: str) -> LiveCallDirection:
    if value in LIVE_CALL_DIRECTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIVE_CALL_DIRECTION_VALUES!r}"
    )
