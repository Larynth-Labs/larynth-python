from typing import Literal

PracticeResultState = Literal["error", "failed", "passed"]

PRACTICE_RESULT_STATE_VALUES: set[PracticeResultState] = {
    "error",
    "failed",
    "passed",
}


def check_practice_result_state(value: str) -> PracticeResultState:
    if value in PRACTICE_RESULT_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRACTICE_RESULT_STATE_VALUES!r}"
    )
