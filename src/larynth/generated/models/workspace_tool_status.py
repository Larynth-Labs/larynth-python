from typing import Literal

WorkspaceToolStatus = Literal["disabled", "failing", "ok"]

WORKSPACE_TOOL_STATUS_VALUES: set[WorkspaceToolStatus] = {
    "disabled",
    "failing",
    "ok",
}


def check_workspace_tool_status(value: str) -> WorkspaceToolStatus:
    if value in WORKSPACE_TOOL_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WORKSPACE_TOOL_STATUS_VALUES!r}"
    )
