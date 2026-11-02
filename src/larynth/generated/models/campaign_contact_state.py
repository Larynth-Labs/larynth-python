from typing import Literal

CampaignContactState = Literal[
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

CAMPAIGN_CONTACT_STATE_VALUES: set[CampaignContactState] = {
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


def check_campaign_contact_state(value: str) -> CampaignContactState:
    if value in CAMPAIGN_CONTACT_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CAMPAIGN_CONTACT_STATE_VALUES!r}"
    )
