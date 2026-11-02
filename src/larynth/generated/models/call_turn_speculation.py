from typing import Literal

CallTurnSpeculation = Literal["discarded", "none", "promoted"]

CALL_TURN_SPECULATION_VALUES: set[CallTurnSpeculation] = {
    "discarded",
    "none",
    "promoted",
}


def check_call_turn_speculation(value: str) -> CallTurnSpeculation:
    if value in CALL_TURN_SPECULATION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_TURN_SPECULATION_VALUES!r}"
    )
