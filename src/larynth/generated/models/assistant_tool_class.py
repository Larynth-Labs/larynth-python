from typing import Literal

AssistantToolClass = Literal["fast", "slow", "terminal"]

ASSISTANT_TOOL_CLASS_VALUES: set[AssistantToolClass] = {
    "fast",
    "slow",
    "terminal",
}


def check_assistant_tool_class(value: str) -> AssistantToolClass:
    if value in ASSISTANT_TOOL_CLASS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ASSISTANT_TOOL_CLASS_VALUES!r}"
    )
