from typing import Literal

AssistantVersionTurnPreset = Literal["balanced", "custom", "patient", "snappy"]

ASSISTANT_VERSION_TURN_PRESET_VALUES: set[AssistantVersionTurnPreset] = {
    "balanced",
    "custom",
    "patient",
    "snappy",
}


def check_assistant_version_turn_preset(value: str) -> AssistantVersionTurnPreset:
    if value in ASSISTANT_VERSION_TURN_PRESET_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ASSISTANT_VERSION_TURN_PRESET_VALUES!r}"
    )
