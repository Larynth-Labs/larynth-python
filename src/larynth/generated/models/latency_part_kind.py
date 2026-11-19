from typing import Literal

LatencyPartKind = Literal["llm", "stt", "tts"]

LATENCY_PART_KIND_VALUES: set[LatencyPartKind] = {
    "llm",
    "stt",
    "tts",
}


def check_latency_part_kind(value: str) -> LatencyPartKind:
    if value in LATENCY_PART_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LATENCY_PART_KIND_VALUES!r}"
    )
