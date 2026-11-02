from typing import Literal

AssistantVersionSpecMode = Literal["cascade", "s2s"]

ASSISTANT_VERSION_SPEC_MODE_VALUES: set[AssistantVersionSpecMode] = {
    "cascade",
    "s2s",
}


def check_assistant_version_spec_mode(value: str) -> AssistantVersionSpecMode:
    if value in ASSISTANT_VERSION_SPEC_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ASSISTANT_VERSION_SPEC_MODE_VALUES!r}"
    )
