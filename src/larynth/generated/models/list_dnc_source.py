from typing import Literal

ListDncSource = Literal[
    "api", "import", "in_call_opt_out", "internal", "operator", "revocation"
]

LIST_DNC_SOURCE_VALUES: set[ListDncSource] = {
    "api",
    "import",
    "in_call_opt_out",
    "internal",
    "operator",
    "revocation",
}


def check_list_dnc_source(value: str) -> ListDncSource:
    if value in LIST_DNC_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_DNC_SOURCE_VALUES!r}"
    )
