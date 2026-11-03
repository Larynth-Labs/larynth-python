from typing import Literal

AssistantType = Literal["flow", "single_prompt"]

ASSISTANT_TYPE_VALUES: set[AssistantType] = {
    "flow",
    "single_prompt",
}


def check_assistant_type(value: str) -> AssistantType:
    if value in ASSISTANT_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ASSISTANT_TYPE_VALUES!r}"
    )
