from typing import Literal

CallRecordingInfoDeletedReason = Literal[
    "data_request", "key_destroyed", "retention", "user"
]

CALL_RECORDING_INFO_DELETED_REASON_VALUES: set[CallRecordingInfoDeletedReason] = {
    "data_request",
    "key_destroyed",
    "retention",
    "user",
}


def check_call_recording_info_deleted_reason(
    value: str,
) -> CallRecordingInfoDeletedReason:
    if value in CALL_RECORDING_INFO_DELETED_REASON_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_RECORDING_INFO_DELETED_REASON_VALUES!r}"
    )
