from typing import Literal

LedgerEntryAccount = Literal["available", "held"]

LEDGER_ENTRY_ACCOUNT_VALUES: set[LedgerEntryAccount] = {
    "available",
    "held",
}


def check_ledger_entry_account(value: str) -> LedgerEntryAccount:
    if value in LEDGER_ENTRY_ACCOUNT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LEDGER_ENTRY_ACCOUNT_VALUES!r}"
    )
