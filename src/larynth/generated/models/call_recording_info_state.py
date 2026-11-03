from typing import Literal

CallRecordingInfoState = Literal["failed", "pending", "purged", "uploaded", "verified"]

CALL_RECORDING_INFO_STATE_VALUES: set[CallRecordingInfoState] = {
    "failed",
    "pending",
    "purged",
    "uploaded",
    "verified",
}


def check_call_recording_info_state(value: str) -> CallRecordingInfoState:
    if value in CALL_RECORDING_INFO_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_RECORDING_INFO_STATE_VALUES!r}"
    )
