from typing import Literal

RevocationChannel = Literal[
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

REVOCATION_CHANNEL_VALUES: set[RevocationChannel] = {
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


def check_revocation_channel(value: str) -> RevocationChannel:
    if value in REVOCATION_CHANNEL_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REVOCATION_CHANNEL_VALUES!r}"
    )
