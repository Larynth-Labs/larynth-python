from typing import Literal

ListAssistantsStatus = Literal["active", "archived"]

LIST_ASSISTANTS_STATUS_VALUES: set[ListAssistantsStatus] = {
    "active",
    "archived",
}


def check_list_assistants_status(value: str) -> ListAssistantsStatus:
    if value in LIST_ASSISTANTS_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_ASSISTANTS_STATUS_VALUES!r}"
    )
