from typing import Literal

LedgerEntryAccount = Literal[
    "available", "bundle_credit", "held", "pending_review", "promo_credit"
]

LEDGER_ENTRY_ACCOUNT_VALUES: set[LedgerEntryAccount] = {
    "available",
    "bundle_credit",
    "held",
    "pending_review",
    "promo_credit",
}


def check_ledger_entry_account(value: str) -> LedgerEntryAccount:
    if value in LEDGER_ENTRY_ACCOUNT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LEDGER_ENTRY_ACCOUNT_VALUES!r}"
    )
