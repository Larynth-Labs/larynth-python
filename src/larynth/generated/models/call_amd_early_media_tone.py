from typing import Literal

CallAmdEarlyMediaTone = Literal["none", "other", "ringback", "sit"]

CALL_AMD_EARLY_MEDIA_TONE_VALUES: set[CallAmdEarlyMediaTone] = {
    "none",
    "other",
    "ringback",
    "sit",
}


def check_call_amd_early_media_tone(value: str) -> CallAmdEarlyMediaTone:
    if value in CALL_AMD_EARLY_MEDIA_TONE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_AMD_EARLY_MEDIA_TONE_VALUES!r}"
    )
