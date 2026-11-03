from typing import Literal

ConversationToolStatus = Literal["error", "ok", "timeout"]

CONVERSATION_TOOL_STATUS_VALUES: set[ConversationToolStatus] = {
    "error",
    "ok",
    "timeout",
}


def check_conversation_tool_status(value: str) -> ConversationToolStatus:
    if value in CONVERSATION_TOOL_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONVERSATION_TOOL_STATUS_VALUES!r}"
    )
