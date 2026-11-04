from typing import Literal

ListRevocationsChannel = Literal[
    "api",
    "dashboard",
    "email",
    "import",
    "in_call",
    "inbound_call",
    "operator",
    "optout_line",
    "other",
    "phone_request",
    "web_form",
]

LIST_REVOCATIONS_CHANNEL_VALUES: set[ListRevocationsChannel] = {
    "api",
    "dashboard",
    "email",
    "import",
    "in_call",
    "inbound_call",
    "operator",
    "optout_line",
    "other",
    "phone_request",
    "web_form",
}


def check_list_revocations_channel(value: str) -> ListRevocationsChannel:
    if value in LIST_REVOCATIONS_CHANNEL_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_REVOCATIONS_CHANNEL_VALUES!r}"
    )
