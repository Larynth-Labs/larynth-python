from typing import Literal

LedgerEntryKind = Literal[
    "adjustment",
    "auto_top_up",
    "hold",
    "number_rental",
    "promo",
    "refund",
    "settle",
    "top_up",
]

LEDGER_ENTRY_KIND_VALUES: set[LedgerEntryKind] = {
    "adjustment",
    "auto_top_up",
    "hold",
    "number_rental",
    "promo",
    "refund",
    "settle",
    "top_up",
}


def check_ledger_entry_kind(value: str) -> LedgerEntryKind:
    if value in LEDGER_ENTRY_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LEDGER_ENTRY_KIND_VALUES!r}"
    )
