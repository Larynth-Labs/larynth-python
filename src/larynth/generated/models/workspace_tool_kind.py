from typing import Literal

WorkspaceToolKind = Literal["http"]

WORKSPACE_TOOL_KIND_VALUES: set[WorkspaceToolKind] = {
    "http",
}


def check_workspace_tool_kind(value: str) -> WorkspaceToolKind:
    if value in WORKSPACE_TOOL_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WORKSPACE_TOOL_KIND_VALUES!r}"
    )
