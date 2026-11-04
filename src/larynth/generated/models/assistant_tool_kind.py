from typing import Literal

AssistantToolKind = Literal[
    "calendar",
    "end_call",
    "http_request",
    "mcp",
    "opt_out",
    "transfer",
    "workspace_http",
]

ASSISTANT_TOOL_KIND_VALUES: set[AssistantToolKind] = {
    "calendar",
    "end_call",
    "http_request",
    "mcp",
    "opt_out",
    "transfer",
    "workspace_http",
}


def check_assistant_tool_kind(value: str) -> AssistantToolKind:
    if value in ASSISTANT_TOOL_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ASSISTANT_TOOL_KIND_VALUES!r}"
    )
