from typing import Literal

CreatePracticeRunInputBodyMode = Literal["text", "voice"]

CREATE_PRACTICE_RUN_INPUT_BODY_MODE_VALUES: set[CreatePracticeRunInputBodyMode] = {
    "text",
    "voice",
}


def check_create_practice_run_input_body_mode(
    value: str,
) -> CreatePracticeRunInputBodyMode:
    if value in CREATE_PRACTICE_RUN_INPUT_BODY_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_PRACTICE_RUN_INPUT_BODY_MODE_VALUES!r}"
    )
