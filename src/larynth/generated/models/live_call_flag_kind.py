from typing import Literal

LiveCallFlagKind = Literal[
    "human_requested", "long_silence", "opt_out", "tool_failing", "transfer_in_progress"
]

LIVE_CALL_FLAG_KIND_VALUES: set[LiveCallFlagKind] = {
    "human_requested",
    "long_silence",
    "opt_out",
    "tool_failing",
    "transfer_in_progress",
}


def check_live_call_flag_kind(value: str) -> LiveCallFlagKind:
    if value in LIVE_CALL_FLAG_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIVE_CALL_FLAG_KIND_VALUES!r}"
    )
