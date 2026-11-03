from typing import Literal

CampaignOutcomeLabel = Literal["machine", "phone_menu"]

CAMPAIGN_OUTCOME_LABEL_VALUES: set[CampaignOutcomeLabel] = {
    "machine",
    "phone_menu",
}


def check_campaign_outcome_label(value: str) -> CampaignOutcomeLabel:
    if value in CAMPAIGN_OUTCOME_LABEL_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CAMPAIGN_OUTCOME_LABEL_VALUES!r}"
    )
