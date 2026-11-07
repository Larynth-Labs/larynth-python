from typing import Literal

McpServerStatus = Literal["connected", "error", "needs_review"]

MCP_SERVER_STATUS_VALUES: set[McpServerStatus] = {
    "connected",
    "error",
    "needs_review",
}


def check_mcp_server_status(value: str) -> McpServerStatus:
    if value in MCP_SERVER_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MCP_SERVER_STATUS_VALUES!r}"
    )
