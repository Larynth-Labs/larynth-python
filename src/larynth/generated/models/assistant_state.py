from typing import Literal

AssistantState = Literal["archived", "draft", "live", "paused"]

ASSISTANT_STATE_VALUES: set[AssistantState] = {
    "archived",
    "draft",
    "live",
    "paused",
}


def check_assistant_state(value: str) -> AssistantState:
    if value in ASSISTANT_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ASSISTANT_STATE_VALUES!r}"
    )
