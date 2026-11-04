from typing import Literal

McpToolState = Literal["approved", "disabled", "drifted", "new"]

MCP_TOOL_STATE_VALUES: set[McpToolState] = {
    "approved",
    "disabled",
    "drifted",
    "new",
}


def check_mcp_tool_state(value: str) -> McpToolState:
    if value in MCP_TOOL_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MCP_TOOL_STATE_VALUES!r}"
    )
