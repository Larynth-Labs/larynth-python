from typing import Literal

PracticeRunDetailState = Literal["done", "error", "queued", "running"]

PRACTICE_RUN_DETAIL_STATE_VALUES: set[PracticeRunDetailState] = {
    "done",
    "error",
    "queued",
    "running",
}


def check_practice_run_detail_state(value: str) -> PracticeRunDetailState:
    if value in PRACTICE_RUN_DETAIL_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRACTICE_RUN_DETAIL_STATE_VALUES!r}"
    )
