from typing import Literal

RateMode = Literal["cascade", "s2s"]

RATE_MODE_VALUES: set[RateMode] = {
    "cascade",
    "s2s",
}


def check_rate_mode(value: str) -> RateMode:
    if value in RATE_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RATE_MODE_VALUES!r}")
