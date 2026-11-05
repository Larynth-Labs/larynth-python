from typing import Literal

RateKind = Literal[
    "branded_brand_month",
    "branded_call",
    "byo_sip_minute",
    "call_minute",
    "forward_minute",
    "number_month",
    "number_month_toll_free",
    "premium_model",
    "premium_voice",
    "transfer_minute",
]

RATE_KIND_VALUES: set[RateKind] = {
    "branded_brand_month",
    "branded_call",
    "byo_sip_minute",
    "call_minute",
    "forward_minute",
    "number_month",
    "number_month_toll_free",
    "premium_model",
    "premium_voice",
    "transfer_minute",
}


def check_rate_kind(value: str) -> RateKind:
    if value in RATE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RATE_KIND_VALUES!r}")
