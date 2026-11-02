from typing import Literal

BalanceCurrency = Literal["USD"]

BALANCE_CURRENCY_VALUES: set[BalanceCurrency] = {
    "USD",
}


def check_balance_currency(value: str) -> BalanceCurrency:
    if value in BALANCE_CURRENCY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BALANCE_CURRENCY_VALUES!r}"
    )
