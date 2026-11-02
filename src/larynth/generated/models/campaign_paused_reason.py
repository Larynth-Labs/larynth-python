from typing import Literal

CampaignPausedReason = Literal[
    "compliance",
    "credits_exhausted",
    "no_caller_id",
    "operator",
    "user",
    "window_closed",
]

CAMPAIGN_PAUSED_REASON_VALUES: set[CampaignPausedReason] = {
    "compliance",
    "credits_exhausted",
    "no_caller_id",
    "operator",
    "user",
    "window_closed",
}


def check_campaign_paused_reason(value: str) -> CampaignPausedReason:
    if value in CAMPAIGN_PAUSED_REASON_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CAMPAIGN_PAUSED_REASON_VALUES!r}"
    )
