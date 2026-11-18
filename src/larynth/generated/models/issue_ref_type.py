from typing import Literal

IssueRefType = Literal["call", "knowledge_gap", "test_run", "tool", "transfer_target"]

ISSUE_REF_TYPE_VALUES: set[IssueRefType] = {
    "call",
    "knowledge_gap",
    "test_run",
    "tool",
    "transfer_target",
}


def check_issue_ref_type(value: str) -> IssueRefType:
    if value in ISSUE_REF_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ISSUE_REF_TYPE_VALUES!r}"
    )
