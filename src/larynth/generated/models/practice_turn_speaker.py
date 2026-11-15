from typing import Literal

PracticeTurnSpeaker = Literal["agent", "caller"]

PRACTICE_TURN_SPEAKER_VALUES: set[PracticeTurnSpeaker] = {
    "agent",
    "caller",
}


def check_practice_turn_speaker(value: str) -> PracticeTurnSpeaker:
    if value in PRACTICE_TURN_SPEAKER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRACTICE_TURN_SPEAKER_VALUES!r}"
    )
