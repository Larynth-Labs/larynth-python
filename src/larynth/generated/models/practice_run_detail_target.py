from typing import Literal

PracticeRunDetailTarget = Literal["draft", "version"]

PRACTICE_RUN_DETAIL_TARGET_VALUES: set[PracticeRunDetailTarget] = {
    "draft",
    "version",
}


def check_practice_run_detail_target(value: str) -> PracticeRunDetailTarget:
    if value in PRACTICE_RUN_DETAIL_TARGET_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRACTICE_RUN_DETAIL_TARGET_VALUES!r}"
    )
