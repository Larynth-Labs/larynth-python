from typing import Literal

CreateCampaignRequestPurpose = Literal["informational", "telemarketing"]

CREATE_CAMPAIGN_REQUEST_PURPOSE_VALUES: set[CreateCampaignRequestPurpose] = {
    "informational",
    "telemarketing",
}


def check_create_campaign_request_purpose(value: str) -> CreateCampaignRequestPurpose:
    if value in CREATE_CAMPAIGN_REQUEST_PURPOSE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_CAMPAIGN_REQUEST_PURPOSE_VALUES!r}"
    )
