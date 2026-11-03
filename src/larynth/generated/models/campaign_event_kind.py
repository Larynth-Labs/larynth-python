from typing import Literal

CampaignEventKind = Literal[
    "ca_preamble_declined",
    "completed",
    "credits_exhausted",
    "dnc_removed_at_dial",
    "held_until_window",
    "opted_out",
    "paused",
    "preflight_passed",
    "resumed",
    "review_decided",
    "review_requested",
    "safeguard_paused",
    "skipped_frequency",
    "skipped_holiday_sunday",
    "started",
]

CAMPAIGN_EVENT_KIND_VALUES: set[CampaignEventKind] = {
    "ca_preamble_declined",
    "completed",
    "credits_exhausted",
    "dnc_removed_at_dial",
    "held_until_window",
    "opted_out",
    "paused",
    "preflight_passed",
    "resumed",
    "review_decided",
    "review_requested",
    "safeguard_paused",
    "skipped_frequency",
    "skipped_holiday_sunday",
    "started",
}


def check_campaign_event_kind(value: str) -> CampaignEventKind:
    if value in CAMPAIGN_EVENT_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CAMPAIGN_EVENT_KIND_VALUES!r}"
    )
