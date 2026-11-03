from typing import Literal

AssistantVersionSpecTurnPreset = Literal["balanced", "custom", "patient", "snappy"]

ASSISTANT_VERSION_SPEC_TURN_PRESET_VALUES: set[AssistantVersionSpecTurnPreset] = {
    "balanced",
    "custom",
    "patient",
    "snappy",
}


def check_assistant_version_spec_turn_preset(
    value: str,
) -> AssistantVersionSpecTurnPreset:
    if value in ASSISTANT_VERSION_SPEC_TURN_PRESET_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ASSISTANT_VERSION_SPEC_TURN_PRESET_VALUES!r}"
    )
