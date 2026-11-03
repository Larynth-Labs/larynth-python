from typing import Literal

CampaignSafeguardState = Literal["cleared", "in_review", "rejected", "review_requested"]

CAMPAIGN_SAFEGUARD_STATE_VALUES: set[CampaignSafeguardState] = {
    "cleared",
    "in_review",
    "rejected",
    "review_requested",
}


def check_campaign_safeguard_state(value: str) -> CampaignSafeguardState:
    if value in CAMPAIGN_SAFEGUARD_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CAMPAIGN_SAFEGUARD_STATE_VALUES!r}"
    )
