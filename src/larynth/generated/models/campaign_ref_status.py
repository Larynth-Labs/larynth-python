from typing import Literal

CampaignRefStatus = Literal["archived", "completed", "draft", "paused", "running"]

CAMPAIGN_REF_STATUS_VALUES: set[CampaignRefStatus] = {
    "archived",
    "completed",
    "draft",
    "paused",
    "running",
}


def check_campaign_ref_status(value: str) -> CampaignRefStatus:
    if value in CAMPAIGN_REF_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CAMPAIGN_REF_STATUS_VALUES!r}"
    )
