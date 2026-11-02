from typing import Literal

ListCampaignContactsState = Literal[
    "completed",
    "dialing",
    "exhausted",
    "failed",
    "in_call",
    "opted_out",
    "pending",
    "retry",
    "skipped",
]

LIST_CAMPAIGN_CONTACTS_STATE_VALUES: set[ListCampaignContactsState] = {
    "completed",
    "dialing",
    "exhausted",
    "failed",
    "in_call",
    "opted_out",
    "pending",
    "retry",
    "skipped",
}


def check_list_campaign_contacts_state(value: str) -> ListCampaignContactsState:
    if value in LIST_CAMPAIGN_CONTACTS_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_CAMPAIGN_CONTACTS_STATE_VALUES!r}"
    )
