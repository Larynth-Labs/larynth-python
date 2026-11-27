from typing import Literal

PracticeRunDetailErrorCode = Literal["practice_run.insufficient_balance"]

PRACTICE_RUN_DETAIL_ERROR_CODE_VALUES: set[PracticeRunDetailErrorCode] = {
    "practice_run.insufficient_balance",
}


def check_practice_run_detail_error_code(value: str) -> PracticeRunDetailErrorCode:
    if value in PRACTICE_RUN_DETAIL_ERROR_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRACTICE_RUN_DETAIL_ERROR_CODE_VALUES!r}"
    )
