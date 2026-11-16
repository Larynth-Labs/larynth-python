from typing import Literal

PracticeRunState = Literal["done", "error", "queued", "running"]

PRACTICE_RUN_STATE_VALUES: set[PracticeRunState] = {
    "done",
    "error",
    "queued",
    "running",
}


def check_practice_run_state(value: str) -> PracticeRunState:
    if value in PRACTICE_RUN_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRACTICE_RUN_STATE_VALUES!r}"
    )
