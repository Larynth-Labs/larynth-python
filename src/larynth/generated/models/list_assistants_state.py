from typing import Literal

ListAssistantsState = Literal["archived", "draft", "live", "paused"]

LIST_ASSISTANTS_STATE_VALUES: set[ListAssistantsState] = {
    "archived",
    "draft",
    "live",
    "paused",
}


def check_list_assistants_state(value: str) -> ListAssistantsState:
    if value in LIST_ASSISTANTS_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_ASSISTANTS_STATE_VALUES!r}"
    )
