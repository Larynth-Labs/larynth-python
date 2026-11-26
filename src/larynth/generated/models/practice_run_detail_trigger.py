from typing import Literal

PracticeRunDetailTrigger = Literal["manual", "publish"]

PRACTICE_RUN_DETAIL_TRIGGER_VALUES: set[PracticeRunDetailTrigger] = {
    "manual",
    "publish",
}


def check_practice_run_detail_trigger(value: str) -> PracticeRunDetailTrigger:
    if value in PRACTICE_RUN_DETAIL_TRIGGER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRACTICE_RUN_DETAIL_TRIGGER_VALUES!r}"
    )
