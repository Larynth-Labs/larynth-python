from typing import Literal

PricePartKind = Literal["base", "llm", "stt", "tts", "voice"]

PRICE_PART_KIND_VALUES: set[PricePartKind] = {
    "base",
    "llm",
    "stt",
    "tts",
    "voice",
}


def check_price_part_kind(value: str) -> PricePartKind:
    if value in PRICE_PART_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRICE_PART_KIND_VALUES!r}"
    )
