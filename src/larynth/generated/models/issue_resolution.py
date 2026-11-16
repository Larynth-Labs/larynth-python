from typing import Literal

IssueResolution = Literal["auto_fixed", "fixed", "no_recent", "not_a_problem"]

ISSUE_RESOLUTION_VALUES: set[IssueResolution] = {
    "auto_fixed",
    "fixed",
    "no_recent",
    "not_a_problem",
}


def check_issue_resolution(value: str) -> IssueResolution:
    if value in ISSUE_RESOLUTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ISSUE_RESOLUTION_VALUES!r}"
    )
