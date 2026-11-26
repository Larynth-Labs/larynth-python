from typing import Literal

PracticeTestSource = Literal["custom", "from_call", "starter"]

PRACTICE_TEST_SOURCE_VALUES: set[PracticeTestSource] = {
    "custom",
    "from_call",
    "starter",
}


def check_practice_test_source(value: str) -> PracticeTestSource:
    if value in PRACTICE_TEST_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRACTICE_TEST_SOURCE_VALUES!r}"
    )
