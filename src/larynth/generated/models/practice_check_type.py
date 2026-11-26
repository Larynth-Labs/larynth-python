from typing import Literal

PracticeCheckType = Literal[
    "judge",
    "not_said",
    "outcome_is",
    "said",
    "tool_args_not_contain",
    "tool_called",
    "tool_not_called",
    "transferred",
]

PRACTICE_CHECK_TYPE_VALUES: set[PracticeCheckType] = {
    "judge",
    "not_said",
    "outcome_is",
    "said",
    "tool_args_not_contain",
    "tool_called",
    "tool_not_called",
    "transferred",
}


def check_practice_check_type(value: str) -> PracticeCheckType:
    if value in PRACTICE_CHECK_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRACTICE_CHECK_TYPE_VALUES!r}"
    )
