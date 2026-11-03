from typing import Literal

UpdateCampaignRequestPurpose = Literal["informational", "telemarketing"]

UPDATE_CAMPAIGN_REQUEST_PURPOSE_VALUES: set[UpdateCampaignRequestPurpose] = {
    "informational",
    "telemarketing",
}


def check_update_campaign_request_purpose(value: str) -> UpdateCampaignRequestPurpose:
    if value in UPDATE_CAMPAIGN_REQUEST_PURPOSE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_CAMPAIGN_REQUEST_PURPOSE_VALUES!r}"
    )
