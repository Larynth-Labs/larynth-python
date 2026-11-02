from typing import Literal

ListCampaignsStatus = Literal["archived", "completed", "draft", "paused", "running"]

LIST_CAMPAIGNS_STATUS_VALUES: set[ListCampaignsStatus] = {
    "archived",
    "completed",
    "draft",
    "paused",
    "running",
}


def check_list_campaigns_status(value: str) -> ListCampaignsStatus:
    if value in LIST_CAMPAIGNS_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_CAMPAIGNS_STATUS_VALUES!r}"
    )
