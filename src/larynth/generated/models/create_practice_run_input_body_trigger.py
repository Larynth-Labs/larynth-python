from typing import Literal

CreatePracticeRunInputBodyTrigger = Literal["manual", "publish"]

CREATE_PRACTICE_RUN_INPUT_BODY_TRIGGER_VALUES: set[
    CreatePracticeRunInputBodyTrigger
] = {
    "manual",
    "publish",
}


def check_create_practice_run_input_body_trigger(
    value: str,
) -> CreatePracticeRunInputBodyTrigger:
    if value in CREATE_PRACTICE_RUN_INPUT_BODY_TRIGGER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_PRACTICE_RUN_INPUT_BODY_TRIGGER_VALUES!r}"
    )
