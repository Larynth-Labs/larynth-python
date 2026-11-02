from typing import Literal

CampaignStatus = Literal["archived", "completed", "draft", "paused", "running"]

CAMPAIGN_STATUS_VALUES: set[CampaignStatus] = {
    "archived",
    "completed",
    "draft",
    "paused",
    "running",
}


def check_campaign_status(value: str) -> CampaignStatus:
    if value in CAMPAIGN_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CAMPAIGN_STATUS_VALUES!r}"
    )
