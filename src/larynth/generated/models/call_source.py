from typing import Literal

CallSource = Literal["widget"]

CALL_SOURCE_VALUES: set[CallSource] = {
    "widget",
}


def check_call_source(value: str) -> CallSource:
    if value in CALL_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_SOURCE_VALUES!r}"
    )
