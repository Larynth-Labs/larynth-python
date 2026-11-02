from typing import Literal

RateDirection = Literal["inbound", "outbound", "web_test"]

RATE_DIRECTION_VALUES: set[RateDirection] = {
    "inbound",
    "outbound",
    "web_test",
}


def check_rate_direction(value: str) -> RateDirection:
    if value in RATE_DIRECTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RATE_DIRECTION_VALUES!r}"
    )
