from typing import Literal

RecordingDeletedReason = Literal["data_request", "key_destroyed", "retention", "user"]

RECORDING_DELETED_REASON_VALUES: set[RecordingDeletedReason] = {
    "data_request",
    "key_destroyed",
    "retention",
    "user",
}


def check_recording_deleted_reason(value: str) -> RecordingDeletedReason:
    if value in RECORDING_DELETED_REASON_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECORDING_DELETED_REASON_VALUES!r}"
    )
