from typing import Literal

CreateCallRequestPurpose = Literal["informational", "telemarketing"]

CREATE_CALL_REQUEST_PURPOSE_VALUES: set[CreateCallRequestPurpose] = {
    "informational",
    "telemarketing",
}


def check_create_call_request_purpose(value: str) -> CreateCallRequestPurpose:
    if value in CREATE_CALL_REQUEST_PURPOSE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_CALL_REQUEST_PURPOSE_VALUES!r}"
    )
