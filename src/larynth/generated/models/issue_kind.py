from typing import Literal

IssueKind = Literal[
    "caller_hung_up",
    "knowledge_gap",
    "missed_booking",
    "no_person_available",
    "reported",
    "said_not_done",
    "test_failed",
    "tool_error",
    "transfer_failed",
    "unresolved_call",
]

ISSUE_KIND_VALUES: set[IssueKind] = {
    "caller_hung_up",
    "knowledge_gap",
    "missed_booking",
    "no_person_available",
    "reported",
    "said_not_done",
    "test_failed",
    "tool_error",
    "transfer_failed",
    "unresolved_call",
}


def check_issue_kind(value: str) -> IssueKind:
    if value in ISSUE_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ISSUE_KIND_VALUES!r}"
    )
