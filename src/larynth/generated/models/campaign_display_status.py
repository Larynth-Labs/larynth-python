from typing import Literal

CampaignDisplayStatus = Literal[
    "archived",
    "blocked",
    "completed",
    "draft",
    "paused",
    "running",
    "safeguard_review",
    "scheduled",
]

CAMPAIGN_DISPLAY_STATUS_VALUES: set[CampaignDisplayStatus] = {
    "archived",
    "blocked",
    "completed",
    "draft",
    "paused",
    "running",
    "safeguard_review",
    "scheduled",
}


def check_campaign_display_status(value: str) -> CampaignDisplayStatus:
    if value in CAMPAIGN_DISPLAY_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CAMPAIGN_DISPLAY_STATUS_VALUES!r}"
    )
