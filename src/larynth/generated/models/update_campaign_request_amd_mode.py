from typing import Literal

UpdateCampaignRequestAmdMode = Literal["hangup_on_machine", "off", "voicemail"]

UPDATE_CAMPAIGN_REQUEST_AMD_MODE_VALUES: set[UpdateCampaignRequestAmdMode] = {
    "hangup_on_machine",
    "off",
    "voicemail",
}


def check_update_campaign_request_amd_mode(value: str) -> UpdateCampaignRequestAmdMode:
    if value in UPDATE_CAMPAIGN_REQUEST_AMD_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_CAMPAIGN_REQUEST_AMD_MODE_VALUES!r}"
    )
