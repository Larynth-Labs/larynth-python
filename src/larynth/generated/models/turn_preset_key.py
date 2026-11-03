from typing import Literal

TurnPresetKey = Literal["balanced", "patient", "snappy"]

TURN_PRESET_KEY_VALUES: set[TurnPresetKey] = {
    "balanced",
    "patient",
    "snappy",
}


def check_turn_preset_key(value: str) -> TurnPresetKey:
    if value in TURN_PRESET_KEY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TURN_PRESET_KEY_VALUES!r}"
    )
