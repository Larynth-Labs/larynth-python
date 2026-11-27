from typing import Literal

PracticeTestDraftSource = Literal["from_call"]

PRACTICE_TEST_DRAFT_SOURCE_VALUES: set[PracticeTestDraftSource] = {
    "from_call",
}


def check_practice_test_draft_source(value: str) -> PracticeTestDraftSource:
    if value in PRACTICE_TEST_DRAFT_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRACTICE_TEST_DRAFT_SOURCE_VALUES!r}"
    )
