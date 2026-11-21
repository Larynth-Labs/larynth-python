from typing import Literal

CallRecordingLaneLane = Literal["agent", "caller"]

CALL_RECORDING_LANE_LANE_VALUES: set[CallRecordingLaneLane] = {
    "agent",
    "caller",
}


def check_call_recording_lane_lane(value: str) -> CallRecordingLaneLane:
    if value in CALL_RECORDING_LANE_LANE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_RECORDING_LANE_LANE_VALUES!r}"
    )
