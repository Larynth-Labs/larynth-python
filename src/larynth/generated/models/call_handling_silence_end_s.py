from typing import Literal

CallHandlingSilenceEndS = Literal[15, 30, 60]

CALL_HANDLING_SILENCE_END_S_VALUES: set[CallHandlingSilenceEndS] = {
    15,
    30,
    60,
}


def check_call_handling_silence_end_s(value: int) -> CallHandlingSilenceEndS:
    if value in CALL_HANDLING_SILENCE_END_S_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_HANDLING_SILENCE_END_S_VALUES!r}"
    )
