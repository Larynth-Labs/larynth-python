from typing import Literal

CallCoverage = Literal[
    "after_hours", "forwarded_busy", "forwarded_no_answer", "holiday", "open"
]

CALL_COVERAGE_VALUES: set[CallCoverage] = {
    "after_hours",
    "forwarded_busy",
    "forwarded_no_answer",
    "holiday",
    "open",
}


def check_call_coverage(value: str) -> CallCoverage:
    if value in CALL_COVERAGE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_COVERAGE_VALUES!r}"
    )
