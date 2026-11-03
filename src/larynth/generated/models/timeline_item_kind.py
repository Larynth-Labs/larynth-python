from typing import Literal

TimelineItemKind = Literal[
    "call",
    "campaign_attempt",
    "campaign_enrolled",
    "consent_granted",
    "consent_revoked",
    "contact_created",
    "dnc_added",
    "dnc_removed",
    "imported",
]

TIMELINE_ITEM_KIND_VALUES: set[TimelineItemKind] = {
    "call",
    "campaign_attempt",
    "campaign_enrolled",
    "consent_granted",
    "consent_revoked",
    "contact_created",
    "dnc_added",
    "dnc_removed",
    "imported",
}


def check_timeline_item_kind(value: str) -> TimelineItemKind:
    if value in TIMELINE_ITEM_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TIMELINE_ITEM_KIND_VALUES!r}"
    )
