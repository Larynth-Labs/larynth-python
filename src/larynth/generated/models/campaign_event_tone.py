from typing import Literal

CampaignEventTone = Literal["neutral", "ok", "stop", "warn"]

CAMPAIGN_EVENT_TONE_VALUES: set[CampaignEventTone] = {
    "neutral",
    "ok",
    "stop",
    "warn",
}


def check_campaign_event_tone(value: str) -> CampaignEventTone:
    if value in CAMPAIGN_EVENT_TONE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CAMPAIGN_EVENT_TONE_VALUES!r}"
    )
