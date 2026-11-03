from typing import Literal

CheckFixKind = Literal["link", "step"]

CHECK_FIX_KIND_VALUES: set[CheckFixKind] = {
    "link",
    "step",
}


def check_check_fix_kind(value: str) -> CheckFixKind:
    if value in CHECK_FIX_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHECK_FIX_KIND_VALUES!r}"
    )
