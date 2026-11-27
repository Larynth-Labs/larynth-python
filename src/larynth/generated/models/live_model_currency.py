from typing import Literal

LiveModelCurrency = Literal["USD"]

LIVE_MODEL_CURRENCY_VALUES: set[LiveModelCurrency] = {
    "USD",
}


def check_live_model_currency(value: str) -> LiveModelCurrency:
    if value in LIVE_MODEL_CURRENCY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIVE_MODEL_CURRENCY_VALUES!r}"
    )
