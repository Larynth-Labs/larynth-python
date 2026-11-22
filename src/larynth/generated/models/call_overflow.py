from typing import Literal

CallOverflow = Literal["abandoned", "answered", "busy_message", "forwarded"]

CALL_OVERFLOW_VALUES: set[CallOverflow] = {
    "abandoned",
    "answered",
    "busy_message",
    "forwarded",
}


def check_call_overflow(value: str) -> CallOverflow:
    if value in CALL_OVERFLOW_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_OVERFLOW_VALUES!r}"
    )
