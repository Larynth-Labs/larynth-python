from typing import Literal

DNCEntryScope = Literal["platform", "tenant"]

DNC_ENTRY_SCOPE_VALUES: set[DNCEntryScope] = {
    "platform",
    "tenant",
}


def check_dnc_entry_scope(value: str) -> DNCEntryScope:
    if value in DNC_ENTRY_SCOPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DNC_ENTRY_SCOPE_VALUES!r}"
    )
