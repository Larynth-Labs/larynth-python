from typing import Literal

LiveCallLineSpeaker = Literal["agent", "caller", "staff"]

LIVE_CALL_LINE_SPEAKER_VALUES: set[LiveCallLineSpeaker] = {
    "agent",
    "caller",
    "staff",
}


def check_live_call_line_speaker(value: str) -> LiveCallLineSpeaker:
    if value in LIVE_CALL_LINE_SPEAKER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIVE_CALL_LINE_SPEAKER_VALUES!r}"
    )
