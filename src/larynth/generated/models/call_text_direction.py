from typing import Literal

CallTextDirection = Literal["in", "out"]

CALL_TEXT_DIRECTION_VALUES: set[CallTextDirection] = {
    "in",
    "out",
}


def check_call_text_direction(value: str) -> CallTextDirection:
    if value in CALL_TEXT_DIRECTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_TEXT_DIRECTION_VALUES!r}"
    )
