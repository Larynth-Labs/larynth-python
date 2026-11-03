from typing import Literal

BulkUpdateContactsRequestAction = Literal[
    "add_tag", "add_to_campaign", "mark_dnc", "remove_tag"
]

BULK_UPDATE_CONTACTS_REQUEST_ACTION_VALUES: set[BulkUpdateContactsRequestAction] = {
    "add_tag",
    "add_to_campaign",
    "mark_dnc",
    "remove_tag",
}


def check_bulk_update_contacts_request_action(
    value: str,
) -> BulkUpdateContactsRequestAction:
    if value in BULK_UPDATE_CONTACTS_REQUEST_ACTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BULK_UPDATE_CONTACTS_REQUEST_ACTION_VALUES!r}"
    )
