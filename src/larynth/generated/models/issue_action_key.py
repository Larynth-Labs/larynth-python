from typing import Literal

IssueActionKey = Literal[
    "add_answer",
    "call_back",
    "check_transfer",
    "open_agent",
    "open_call",
    "open_tool",
    "reconnect_tool",
    "set_up_transfer",
]

ISSUE_ACTION_KEY_VALUES: set[IssueActionKey] = {
    "add_answer",
    "call_back",
    "check_transfer",
    "open_agent",
    "open_call",
    "open_tool",
    "reconnect_tool",
    "set_up_transfer",
}


def check_issue_action_key(value: str) -> IssueActionKey:
    if value in ISSUE_ACTION_KEY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ISSUE_ACTION_KEY_VALUES!r}"
    )
