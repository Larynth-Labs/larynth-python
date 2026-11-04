from typing import Literal

ListContactsOrder = Literal["-created", "-last_contact", "name"]

LIST_CONTACTS_ORDER_VALUES: set[ListContactsOrder] = {
    "-created",
    "-last_contact",
    "name",
}


def check_list_contacts_order(value: str) -> ListContactsOrder:
    if value in LIST_CONTACTS_ORDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_CONTACTS_ORDER_VALUES!r}"
    )
