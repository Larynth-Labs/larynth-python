from typing import Literal

AssistantVersionMode = Literal["cascade", "s2s"]

ASSISTANT_VERSION_MODE_VALUES: set[AssistantVersionMode] = {
    "cascade",
    "s2s",
}


def check_assistant_version_mode(value: str) -> AssistantVersionMode:
    if value in ASSISTANT_VERSION_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ASSISTANT_VERSION_MODE_VALUES!r}"
    )
