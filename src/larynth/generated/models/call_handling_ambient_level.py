from typing import Literal

CallHandlingAmbientLevel = Literal["high", "low", "medium"]

CALL_HANDLING_AMBIENT_LEVEL_VALUES: set[CallHandlingAmbientLevel] = {
    "high",
    "low",
    "medium",
}


def check_call_handling_ambient_level(value: str) -> CallHandlingAmbientLevel:
    if value in CALL_HANDLING_AMBIENT_LEVEL_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_HANDLING_AMBIENT_LEVEL_VALUES!r}"
    )
