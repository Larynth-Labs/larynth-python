from typing import Literal

AssistantDraftMode = Literal["cascade", "s2s"]

ASSISTANT_DRAFT_MODE_VALUES: set[AssistantDraftMode] = {
    "cascade",
    "s2s",
}


def check_assistant_draft_mode(value: str) -> AssistantDraftMode:
    if value in ASSISTANT_DRAFT_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ASSISTANT_DRAFT_MODE_VALUES!r}"
    )
