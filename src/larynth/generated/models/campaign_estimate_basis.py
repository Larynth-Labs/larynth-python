from typing import Literal

CampaignEstimateBasis = Literal["platform_default", "tenant_history"]

CAMPAIGN_ESTIMATE_BASIS_VALUES: set[CampaignEstimateBasis] = {
    "platform_default",
    "tenant_history",
}


def check_campaign_estimate_basis(value: str) -> CampaignEstimateBasis:
    if value in CAMPAIGN_ESTIMATE_BASIS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CAMPAIGN_ESTIMATE_BASIS_VALUES!r}"
    )
