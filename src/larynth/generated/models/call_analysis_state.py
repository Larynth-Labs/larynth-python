from typing import Literal

CallAnalysisState = Literal["done", "failed", "pending", "skipped"]

CALL_ANALYSIS_STATE_VALUES: set[CallAnalysisState] = {
    "done",
    "failed",
    "pending",
    "skipped",
}


def check_call_analysis_state(value: str) -> CallAnalysisState:
    if value in CALL_ANALYSIS_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_ANALYSIS_STATE_VALUES!r}"
    )
