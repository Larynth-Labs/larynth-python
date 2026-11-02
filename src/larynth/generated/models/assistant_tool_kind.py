from typing import Literal

AssistantToolKind = Literal["end_call", "http_request", "opt_out", "transfer"]

ASSISTANT_TOOL_KIND_VALUES: set[AssistantToolKind] = {
    "end_call",
    "http_request",
    "opt_out",
    "transfer",
}


def check_assistant_tool_kind(value: str) -> AssistantToolKind:
    if value in ASSISTANT_TOOL_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ASSISTANT_TOOL_KIND_VALUES!r}"
    )
