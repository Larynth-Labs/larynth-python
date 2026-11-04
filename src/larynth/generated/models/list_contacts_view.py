from typing import Literal

ListContactsView = Literal["all", "callable", "dnc", "needs_consent"]

LIST_CONTACTS_VIEW_VALUES: set[ListContactsView] = {
    "all",
    "callable",
    "dnc",
    "needs_consent",
}


def check_list_contacts_view(value: str) -> ListContactsView:
    if value in LIST_CONTACTS_VIEW_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_CONTACTS_VIEW_VALUES!r}"
    )
