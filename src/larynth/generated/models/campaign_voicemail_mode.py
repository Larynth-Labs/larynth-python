from typing import Literal

CampaignVoicemailMode = Literal["agent", "hangup", "message", "off"]

CAMPAIGN_VOICEMAIL_MODE_VALUES: set[CampaignVoicemailMode] = {
    "agent",
    "hangup",
    "message",
    "off",
}


def check_campaign_voicemail_mode(value: str) -> CampaignVoicemailMode:
    if value in CAMPAIGN_VOICEMAIL_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CAMPAIGN_VOICEMAIL_MODE_VALUES!r}"
    )
