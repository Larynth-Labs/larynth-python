from typing import Literal

RateCardLineRounding = Literal["none", "started_minute"]

RATE_CARD_LINE_ROUNDING_VALUES: set[RateCardLineRounding] = {
    "none",
    "started_minute",
}


def check_rate_card_line_rounding(value: str) -> RateCardLineRounding:
    if value in RATE_CARD_LINE_ROUNDING_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RATE_CARD_LINE_ROUNDING_VALUES!r}"
    )
