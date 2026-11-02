from typing import Literal

RateCurrency = Literal["USD"]

RATE_CURRENCY_VALUES: set[RateCurrency] = {
    "USD",
}


def check_rate_currency(value: str) -> RateCurrency:
    if value in RATE_CURRENCY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RATE_CURRENCY_VALUES!r}"
    )
