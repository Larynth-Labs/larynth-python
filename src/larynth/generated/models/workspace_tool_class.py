from typing import Literal

WorkspaceToolClass = Literal["fast", "slow"]

WORKSPACE_TOOL_CLASS_VALUES: set[WorkspaceToolClass] = {
    "fast",
    "slow",
}


def check_workspace_tool_class(value: str) -> WorkspaceToolClass:
    if value in WORKSPACE_TOOL_CLASS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WORKSPACE_TOOL_CLASS_VALUES!r}"
    )
