from typing import Literal

PracticeRunErrorCode = Literal["practice_run.insufficient_balance"]

PRACTICE_RUN_ERROR_CODE_VALUES: set[PracticeRunErrorCode] = {
    "practice_run.insufficient_balance",
}


def check_practice_run_error_code(value: str) -> PracticeRunErrorCode:
    if value in PRACTICE_RUN_ERROR_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRACTICE_RUN_ERROR_CODE_VALUES!r}"
    )
