from typing import Literal

ListLedgerKind = Literal[
    "adjustment",
    "auto_top_up",
    "bundle_conversion",
    "bundle_purchase",
    "hold",
    "number_rental",
    "promo",
    "refund",
    "review_release",
    "settle",
    "top_up",
]

LIST_LEDGER_KIND_VALUES: set[ListLedgerKind] = {
    "adjustment",
    "auto_top_up",
    "bundle_conversion",
    "bundle_purchase",
    "hold",
    "number_rental",
    "promo",
    "refund",
    "review_release",
    "settle",
    "top_up",
}


def check_list_ledger_kind(value: str) -> ListLedgerKind:
    if value in LIST_LEDGER_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_LEDGER_KIND_VALUES!r}"
    )
