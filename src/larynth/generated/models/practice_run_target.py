from typing import Literal

PracticeRunTarget = Literal["draft", "version"]

PRACTICE_RUN_TARGET_VALUES: set[PracticeRunTarget] = {
    "draft",
    "version",
}


def check_practice_run_target(value: str) -> PracticeRunTarget:
    if value in PRACTICE_RUN_TARGET_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRACTICE_RUN_TARGET_VALUES!r}"
    )
