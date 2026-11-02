from typing import Literal

CampaignAmdMode = Literal["hangup_on_machine", "off", "voicemail"]

CAMPAIGN_AMD_MODE_VALUES: set[CampaignAmdMode] = {
    "hangup_on_machine",
    "off",
    "voicemail",
}


def check_campaign_amd_mode(value: str) -> CampaignAmdMode:
    if value in CAMPAIGN_AMD_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CAMPAIGN_AMD_MODE_VALUES!r}"
    )
