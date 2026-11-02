from typing import Literal

CallMode = Literal["cascade", "s2s"]

CALL_MODE_VALUES: set[CallMode] = {
    "cascade",
    "s2s",
}


def check_call_mode(value: str) -> CallMode:
    if value in CALL_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CALL_MODE_VALUES!r}")
