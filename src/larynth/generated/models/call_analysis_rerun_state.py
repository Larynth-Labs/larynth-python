from typing import Literal

CallAnalysisRerunState = Literal["pending"]

CALL_ANALYSIS_RERUN_STATE_VALUES: set[CallAnalysisRerunState] = {
    "pending",
}


def check_call_analysis_rerun_state(value: str) -> CallAnalysisRerunState:
    if value in CALL_ANALYSIS_RERUN_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_ANALYSIS_RERUN_STATE_VALUES!r}"
    )
