from typing import Literal

DncCheckList = Literal["national", "opt_out", "platform", "tenant"]

DNC_CHECK_LIST_VALUES: set[DncCheckList] = {
    "national",
    "opt_out",
    "platform",
    "tenant",
}


def check_dnc_check_list(value: str) -> DncCheckList:
    if value in DNC_CHECK_LIST_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DNC_CHECK_LIST_VALUES!r}"
    )
