from typing import Literal

CreateCampaignRequestAmdMode = Literal["hangup_on_machine", "off", "voicemail"]

CREATE_CAMPAIGN_REQUEST_AMD_MODE_VALUES: set[CreateCampaignRequestAmdMode] = {
    "hangup_on_machine",
    "off",
    "voicemail",
}


def check_create_campaign_request_amd_mode(value: str) -> CreateCampaignRequestAmdMode:
    if value in CREATE_CAMPAIGN_REQUEST_AMD_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_CAMPAIGN_REQUEST_AMD_MODE_VALUES!r}"
    )
