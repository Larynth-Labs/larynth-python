from typing import Literal

ListPracticeResultsState = Literal["error", "failed", "passed"]

LIST_PRACTICE_RESULTS_STATE_VALUES: set[ListPracticeResultsState] = {
    "error",
    "failed",
    "passed",
}


def check_list_practice_results_state(value: str) -> ListPracticeResultsState:
    if value in LIST_PRACTICE_RESULTS_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_PRACTICE_RESULTS_STATE_VALUES!r}"
    )
