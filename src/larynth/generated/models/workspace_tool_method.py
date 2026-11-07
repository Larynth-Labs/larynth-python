from typing import Literal

WorkspaceToolMethod = Literal["DELETE", "GET", "PATCH", "POST", "PUT"]

WORKSPACE_TOOL_METHOD_VALUES: set[WorkspaceToolMethod] = {
    "DELETE",
    "GET",
    "PATCH",
    "POST",
    "PUT",
}


def check_workspace_tool_method(value: str) -> WorkspaceToolMethod:
    if value in WORKSPACE_TOOL_METHOD_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WORKSPACE_TOOL_METHOD_VALUES!r}"
    )
