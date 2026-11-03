from typing import Literal

AssistantDraftTurnPreset = Literal["balanced", "custom", "patient", "snappy"]

ASSISTANT_DRAFT_TURN_PRESET_VALUES: set[AssistantDraftTurnPreset] = {
    "balanced",
    "custom",
    "patient",
    "snappy",
}


def check_assistant_draft_turn_preset(value: str) -> AssistantDraftTurnPreset:
    if value in ASSISTANT_DRAFT_TURN_PRESET_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ASSISTANT_DRAFT_TURN_PRESET_VALUES!r}"
    )
