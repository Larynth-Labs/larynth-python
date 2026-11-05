from typing import Literal

RateCardGroupKey = Literal[
    "branded", "calls", "free", "numbers", "premium", "simulations", "telephony"
]

RATE_CARD_GROUP_KEY_VALUES: set[RateCardGroupKey] = {
    "branded",
    "calls",
    "free",
    "numbers",
    "premium",
    "simulations",
    "telephony",
}


def check_rate_card_group_key(value: str) -> RateCardGroupKey:
    if value in RATE_CARD_GROUP_KEY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RATE_CARD_GROUP_KEY_VALUES!r}"
    )
