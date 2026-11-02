from typing import Literal

ListLedgerAccount = Literal["available", "held"]

LIST_LEDGER_ACCOUNT_VALUES: set[ListLedgerAccount] = {
    "available",
    "held",
}


def check_list_ledger_account(value: str) -> ListLedgerAccount:
    if value in LIST_LEDGER_ACCOUNT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_LEDGER_ACCOUNT_VALUES!r}"
    )
