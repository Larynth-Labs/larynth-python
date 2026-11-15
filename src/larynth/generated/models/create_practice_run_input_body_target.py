from typing import Literal

CreatePracticeRunInputBodyTarget = Literal["draft", "version"]

CREATE_PRACTICE_RUN_INPUT_BODY_TARGET_VALUES: set[CreatePracticeRunInputBodyTarget] = {
    "draft",
    "version",
}


def check_create_practice_run_input_body_target(
    value: str,
) -> CreatePracticeRunInputBodyTarget:
    if value in CREATE_PRACTICE_RUN_INPUT_BODY_TARGET_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_PRACTICE_RUN_INPUT_BODY_TARGET_VALUES!r}"
    )
