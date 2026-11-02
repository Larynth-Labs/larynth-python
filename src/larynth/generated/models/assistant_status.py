from typing import Literal

AssistantStatus = Literal["active", "archived"]

ASSISTANT_STATUS_VALUES: set[AssistantStatus] = {
    "active",
    "archived",
}


def check_assistant_status(value: str) -> AssistantStatus:
    if value in ASSISTANT_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ASSISTANT_STATUS_VALUES!r}"
    )
