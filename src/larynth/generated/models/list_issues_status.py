from typing import Literal

ListIssuesStatus = Literal["ignored", "open", "resolved"]

LIST_ISSUES_STATUS_VALUES: set[ListIssuesStatus] = {
    "ignored",
    "open",
    "resolved",
}


def check_list_issues_status(value: str) -> ListIssuesStatus:
    if value in LIST_ISSUES_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_ISSUES_STATUS_VALUES!r}"
    )
