from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.campaign import Campaign
    from ..models.campaign_counts import CampaignCounts


T = TypeVar("T", bound="CampaignPage")


@_attrs_define
class CampaignPage:
    """
    Attributes:
        counts (CampaignCounts):
        data (list[Campaign]):
        next_cursor (None | str):
    """

    counts: CampaignCounts
    data: list[Campaign]
    next_cursor: None | str

    def to_dict(self) -> dict[str, Any]:
        counts = self.counts.to_dict()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        next_cursor: None | str
        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "counts": counts,
                "data": data,
                "next_cursor": next_cursor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.campaign import Campaign
        from ..models.campaign_counts import CampaignCounts

        d = dict(src_dict)
        counts = CampaignCounts.from_dict(d.pop("counts"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = Campaign.from_dict(data_item_data)

            data.append(data_item)

        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        campaign_page = cls(
            counts=counts,
            data=data,
            next_cursor=next_cursor,
        )

        return campaign_page
