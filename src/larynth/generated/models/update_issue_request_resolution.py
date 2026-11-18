from typing import Literal

UpdateIssueRequestResolution = Literal["fixed", "not_a_problem"]

UPDATE_ISSUE_REQUEST_RESOLUTION_VALUES: set[UpdateIssueRequestResolution] = {
    "fixed",
    "not_a_problem",
}


def check_update_issue_request_resolution(value: str) -> UpdateIssueRequestResolution:
    if value in UPDATE_ISSUE_REQUEST_RESOLUTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ISSUE_REQUEST_RESOLUTION_VALUES!r}"
    )
