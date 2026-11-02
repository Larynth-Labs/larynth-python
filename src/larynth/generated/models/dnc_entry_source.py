from typing import Literal

DNCEntrySource = Literal[
    "api", "import", "in_call_opt_out", "internal", "operator", "revocation"
]

DNC_ENTRY_SOURCE_VALUES: set[DNCEntrySource] = {
    "api",
    "import",
    "in_call_opt_out",
    "internal",
    "operator",
    "revocation",
}


def check_dnc_entry_source(value: str) -> DNCEntrySource:
    if value in DNC_ENTRY_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DNC_ENTRY_SOURCE_VALUES!r}"
    )
