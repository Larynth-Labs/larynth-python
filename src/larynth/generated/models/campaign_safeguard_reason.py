from typing import Literal

CampaignSafeguardReason = Literal[
    "abandonment",
    "carrier_blocking",
    "complaints",
    "optout_rate",
    "script_flag",
    "short_calls",
]

CAMPAIGN_SAFEGUARD_REASON_VALUES: set[CampaignSafeguardReason] = {
    "abandonment",
    "carrier_blocking",
    "complaints",
    "optout_rate",
    "script_flag",
    "short_calls",
}


def check_campaign_safeguard_reason(value: str) -> CampaignSafeguardReason:
    if value in CAMPAIGN_SAFEGUARD_REASON_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CAMPAIGN_SAFEGUARD_REASON_VALUES!r}"
    )
