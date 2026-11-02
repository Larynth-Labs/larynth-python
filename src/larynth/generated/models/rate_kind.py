from typing import Literal

RateKind = Literal["call_minute", "number_month", "transfer_minute"]

RATE_KIND_VALUES: set[RateKind] = {
    "call_minute",
    "number_month",
    "transfer_minute",
}


def check_rate_kind(value: str) -> RateKind:
    if value in RATE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RATE_KIND_VALUES!r}")
