from typing import Literal

CampaignPurpose = Literal["informational", "telemarketing"]

CAMPAIGN_PURPOSE_VALUES: set[CampaignPurpose] = {
    "informational",
    "telemarketing",
}


def check_campaign_purpose(value: str) -> CampaignPurpose:
    if value in CAMPAIGN_PURPOSE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CAMPAIGN_PURPOSE_VALUES!r}"
    )
