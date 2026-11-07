from typing import Literal

McpServerTransport = Literal["streamable_http"]

MCP_SERVER_TRANSPORT_VALUES: set[McpServerTransport] = {
    "streamable_http",
}


def check_mcp_server_transport(value: str) -> McpServerTransport:
    if value in MCP_SERVER_TRANSPORT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MCP_SERVER_TRANSPORT_VALUES!r}"
    )
