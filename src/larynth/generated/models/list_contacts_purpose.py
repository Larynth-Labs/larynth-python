from typing import Literal

ListContactsPurpose = Literal["informational", "telemarketing"]

LIST_CONTACTS_PURPOSE_VALUES: set[ListContactsPurpose] = {
    "informational",
    "telemarketing",
}


def check_list_contacts_purpose(value: str) -> ListContactsPurpose:
    if value in LIST_CONTACTS_PURPOSE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_CONTACTS_PURPOSE_VALUES!r}"
    )
