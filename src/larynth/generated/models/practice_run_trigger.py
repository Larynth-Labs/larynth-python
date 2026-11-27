from typing import Literal

PracticeRunTrigger = Literal["manual", "publish"]

PRACTICE_RUN_TRIGGER_VALUES: set[PracticeRunTrigger] = {
    "manual",
    "publish",
}


def check_practice_run_trigger(value: str) -> PracticeRunTrigger:
    if value in PRACTICE_RUN_TRIGGER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRACTICE_RUN_TRIGGER_VALUES!r}"
    )
