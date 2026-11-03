from typing import Literal

PreviewCampaignAudienceRequestPurpose = Literal["informational", "telemarketing"]

PREVIEW_CAMPAIGN_AUDIENCE_REQUEST_PURPOSE_VALUES: set[
    PreviewCampaignAudienceRequestPurpose
] = {
    "informational",
    "telemarketing",
}


def check_preview_campaign_audience_request_purpose(
    value: str,
) -> PreviewCampaignAudienceRequestPurpose:
    if value in PREVIEW_CAMPAIGN_AUDIENCE_REQUEST_PURPOSE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PREVIEW_CAMPAIGN_AUDIENCE_REQUEST_PURPOSE_VALUES!r}"
    )
