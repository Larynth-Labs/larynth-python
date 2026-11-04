from typing import Literal

AfterHoursTargetMode = Literal["assistant", "forward", "same_agent", "take_message"]

AFTER_HOURS_TARGET_MODE_VALUES: set[AfterHoursTargetMode] = {
    "assistant",
    "forward",
    "same_agent",
    "take_message",
}


def check_after_hours_target_mode(value: str) -> AfterHoursTargetMode:
    if value in AFTER_HOURS_TARGET_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AFTER_HOURS_TARGET_MODE_VALUES!r}"
    )
