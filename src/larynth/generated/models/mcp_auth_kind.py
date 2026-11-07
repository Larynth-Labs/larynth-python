from typing import Literal

McpAuthKind = Literal["bearer", "header", "none"]

MCP_AUTH_KIND_VALUES: set[McpAuthKind] = {
    "bearer",
    "header",
    "none",
}


def check_mcp_auth_kind(value: str) -> McpAuthKind:
    if value in MCP_AUTH_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MCP_AUTH_KIND_VALUES!r}"
    )
