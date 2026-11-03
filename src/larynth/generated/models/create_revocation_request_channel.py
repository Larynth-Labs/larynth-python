from typing import Literal

CreateRevocationRequestChannel = Literal[
    "dashboard", "email", "other", "phone_request", "web_form"
]

CREATE_REVOCATION_REQUEST_CHANNEL_VALUES: set[CreateRevocationRequestChannel] = {
    "dashboard",
    "email",
    "other",
    "phone_request",
    "web_form",
}


def check_create_revocation_request_channel(
    value: str,
) -> CreateRevocationRequestChannel:
    if value in CREATE_REVOCATION_REQUEST_CHANNEL_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_REVOCATION_REQUEST_CHANNEL_VALUES!r}"
    )
