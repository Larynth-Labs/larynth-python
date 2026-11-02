from typing import Literal

RecordingState = Literal["failed", "pending", "purged", "uploaded", "verified"]

RECORDING_STATE_VALUES: set[RecordingState] = {
    "failed",
    "pending",
    "purged",
    "uploaded",
    "verified",
}


def check_recording_state(value: str) -> RecordingState:
    if value in RECORDING_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RECORDING_STATE_VALUES!r}"
    )
