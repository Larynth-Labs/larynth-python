from typing import Literal

AssistantSource = Literal["duplicate", "import", "manual", "setup", "template"]

ASSISTANT_SOURCE_VALUES: set[AssistantSource] = {
    "duplicate",
    "import",
    "manual",
    "setup",
    "template",
}


def check_assistant_source(value: str) -> AssistantSource:
    if value in ASSISTANT_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ASSISTANT_SOURCE_VALUES!r}"
    )
