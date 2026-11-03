from typing import Literal

ListCampaignsDisplayStatus = Literal[
    "archived",
    "blocked",
    "completed",
    "draft",
    "paused",
    "running",
    "safeguard_review",
    "scheduled",
]

LIST_CAMPAIGNS_DISPLAY_STATUS_VALUES: set[ListCampaignsDisplayStatus] = {
    "archived",
    "blocked",
    "completed",
    "draft",
    "paused",
    "running",
    "safeguard_review",
    "scheduled",
}


def check_list_campaigns_display_status(value: str) -> ListCampaignsDisplayStatus:
    if value in LIST_CAMPAIGNS_DISPLAY_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_CAMPAIGNS_DISPLAY_STATUS_VALUES!r}"
    )
