from typing import Literal

WorkspaceToolInputMethod = Literal["DELETE", "GET", "PATCH", "POST", "PUT"]

WORKSPACE_TOOL_INPUT_METHOD_VALUES: set[WorkspaceToolInputMethod] = {
    "DELETE",
    "GET",
    "PATCH",
    "POST",
    "PUT",
}


def check_workspace_tool_input_method(value: str) -> WorkspaceToolInputMethod:
    if value in WORKSPACE_TOOL_INPUT_METHOD_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WORKSPACE_TOOL_INPUT_METHOD_VALUES!r}"
    )
