from typing import Literal

CallRecordingInfoLanesItem = Literal["agent", "caller"]

CALL_RECORDING_INFO_LANES_ITEM_VALUES: set[CallRecordingInfoLanesItem] = {
    "agent",
    "caller",
}


def check_call_recording_info_lanes_item(value: str) -> CallRecordingInfoLanesItem:
    if value in CALL_RECORDING_INFO_LANES_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_RECORDING_INFO_LANES_ITEM_VALUES!r}"
    )
