from typing import Literal

RevocationChannel = Literal[
    "api", "dashboard", "import", "in_call", "inbound_call", "operator", "other"
]

REVOCATION_CHANNEL_VALUES: set[RevocationChannel] = {
    "api",
    "dashboard",
    "import",
    "in_call",
    "inbound_call",
    "operator",
    "other",
}


def check_revocation_channel(value: str) -> RevocationChannel:
    if value in REVOCATION_CHANNEL_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REVOCATION_CHANNEL_VALUES!r}"
    )
