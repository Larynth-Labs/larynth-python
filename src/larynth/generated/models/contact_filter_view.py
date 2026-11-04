from typing import Literal

ContactFilterView = Literal["all", "callable", "dnc", "needs_consent"]

CONTACT_FILTER_VIEW_VALUES: set[ContactFilterView] = {
    "all",
    "callable",
    "dnc",
    "needs_consent",
}


def check_contact_filter_view(value: str) -> ContactFilterView:
    if value in CONTACT_FILTER_VIEW_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACT_FILTER_VIEW_VALUES!r}"
    )
