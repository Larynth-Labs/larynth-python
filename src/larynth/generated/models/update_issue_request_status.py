from typing import Literal

UpdateIssueRequestStatus = Literal["ignored", "open", "resolved"]

UPDATE_ISSUE_REQUEST_STATUS_VALUES: set[UpdateIssueRequestStatus] = {
    "ignored",
    "open",
    "resolved",
}


def check_update_issue_request_status(value: str) -> UpdateIssueRequestStatus:
    if value in UPDATE_ISSUE_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ISSUE_REQUEST_STATUS_VALUES!r}"
    )
