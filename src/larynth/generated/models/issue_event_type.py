from typing import Literal

IssueEventType = Literal[
    "assigned", "auto_closed", "ignored", "note", "opened", "reopened", "resolved"
]

ISSUE_EVENT_TYPE_VALUES: set[IssueEventType] = {
    "assigned",
    "auto_closed",
    "ignored",
    "note",
    "opened",
    "reopened",
    "resolved",
}


def check_issue_event_type(value: str) -> IssueEventType:
    if value in ISSUE_EVENT_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ISSUE_EVENT_TYPE_VALUES!r}"
    )
