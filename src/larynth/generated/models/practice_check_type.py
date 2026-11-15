from typing import Literal

PracticeCheckType = Literal[
    "judge", "not_said", "said", "tool_called", "tool_not_called"
]

PRACTICE_CHECK_TYPE_VALUES: set[PracticeCheckType] = {
    "judge",
    "not_said",
    "said",
    "tool_called",
    "tool_not_called",
}


def check_practice_check_type(value: str) -> PracticeCheckType:
    if value in PRACTICE_CHECK_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRACTICE_CHECK_TYPE_VALUES!r}"
    )
