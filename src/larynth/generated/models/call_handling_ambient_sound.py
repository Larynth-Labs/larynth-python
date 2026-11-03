from typing import Literal

CallHandlingAmbientSound = Literal["cafe", "call_center", "office"]

CALL_HANDLING_AMBIENT_SOUND_VALUES: set[CallHandlingAmbientSound] = {
    "cafe",
    "call_center",
    "office",
}


def check_call_handling_ambient_sound(value: str) -> CallHandlingAmbientSound:
    if value in CALL_HANDLING_AMBIENT_SOUND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_HANDLING_AMBIENT_SOUND_VALUES!r}"
    )
