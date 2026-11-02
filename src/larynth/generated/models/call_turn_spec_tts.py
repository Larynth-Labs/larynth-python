from typing import Literal

CallTurnSpecTts = Literal["discarded", "failed", "none", "promoted"]

CALL_TURN_SPEC_TTS_VALUES: set[CallTurnSpecTts] = {
    "discarded",
    "failed",
    "none",
    "promoted",
}


def check_call_turn_spec_tts(value: str) -> CallTurnSpecTts:
    if value in CALL_TURN_SPEC_TTS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_TURN_SPEC_TTS_VALUES!r}"
    )
