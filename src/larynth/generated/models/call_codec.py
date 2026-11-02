from typing import Literal

CallCodec = Literal["G722", "opus", "PCMA", "PCMU"]

CALL_CODEC_VALUES: set[CallCodec] = {
    "G722",
    "opus",
    "PCMA",
    "PCMU",
}


def check_call_codec(value: str) -> CallCodec:
    if value in CALL_CODEC_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_CODEC_VALUES!r}"
    )
