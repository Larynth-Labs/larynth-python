from typing import Literal

WorkspaceToolInputClass = Literal["fast", "slow"]

WORKSPACE_TOOL_INPUT_CLASS_VALUES: set[WorkspaceToolInputClass] = {
    "fast",
    "slow",
}


def check_workspace_tool_input_class(value: str) -> WorkspaceToolInputClass:
    if value in WORKSPACE_TOOL_INPUT_CLASS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WORKSPACE_TOOL_INPUT_CLASS_VALUES!r}"
    )
