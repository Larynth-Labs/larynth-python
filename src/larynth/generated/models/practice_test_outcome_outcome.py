from typing import Literal

PracticeTestOutcomeOutcome = Literal["error", "failed", "mixed", "passed"]

PRACTICE_TEST_OUTCOME_OUTCOME_VALUES: set[PracticeTestOutcomeOutcome] = {
    "error",
    "failed",
    "mixed",
    "passed",
}


def check_practice_test_outcome_outcome(value: str) -> PracticeTestOutcomeOutcome:
    if value in PRACTICE_TEST_OUTCOME_OUTCOME_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRACTICE_TEST_OUTCOME_OUTCOME_VALUES!r}"
    )
