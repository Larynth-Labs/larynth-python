from typing import Literal

CreateCallRequestAmdMode = Literal["hangup_on_machine", "off", "voicemail"]

CREATE_CALL_REQUEST_AMD_MODE_VALUES: set[CreateCallRequestAmdMode] = {
    "hangup_on_machine",
    "off",
    "voicemail",
}


def check_create_call_request_amd_mode(value: str) -> CreateCallRequestAmdMode:
    if value in CREATE_CALL_REQUEST_AMD_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_CALL_REQUEST_AMD_MODE_VALUES!r}"
    )
