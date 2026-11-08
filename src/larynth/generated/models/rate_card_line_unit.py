from typing import Literal

RateCardLineUnit = Literal["at_cost", "free", "per_display", "per_minute", "per_month"]

RATE_CARD_LINE_UNIT_VALUES: set[RateCardLineUnit] = {
    "at_cost",
    "free",
    "per_display",
    "per_minute",
    "per_month",
}


def check_rate_card_line_unit(value: str) -> RateCardLineUnit:
    if value in RATE_CARD_LINE_UNIT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RATE_CARD_LINE_UNIT_VALUES!r}"
    )
