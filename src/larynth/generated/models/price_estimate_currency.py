from typing import Literal

PriceEstimateCurrency = Literal["USD"]

PRICE_ESTIMATE_CURRENCY_VALUES: set[PriceEstimateCurrency] = {
    "USD",
}


def check_price_estimate_currency(value: str) -> PriceEstimateCurrency:
    if value in PRICE_ESTIMATE_CURRENCY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRICE_ESTIMATE_CURRENCY_VALUES!r}"
    )
