from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.campaign_ref import CampaignRef


T = TypeVar("T", bound="NumberUsage")


@_attrs_define
class NumberUsage:
    """
    Attributes:
        campaigns (list[CampaignRef]):
        can_call_out (bool): An active Larynth-owned number; imported numbers never qualify
        optout_line (bool):
    """

    campaigns: list[CampaignRef]
    can_call_out: bool
    optout_line: bool

    def to_dict(self) -> dict[str, Any]:
        campaigns = []
        for campaigns_item_data in self.campaigns:
            campaigns_item = campaigns_item_data.to_dict()
            campaigns.append(campaigns_item)

        can_call_out = self.can_call_out

        optout_line = self.optout_line

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "campaigns": campaigns,
                "can_call_out": can_call_out,
                "optout_line": optout_line,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.campaign_ref import CampaignRef

        d = dict(src_dict)
        campaigns = []
        _campaigns = d.pop("campaigns")
        for campaigns_item_data in _campaigns:
            campaigns_item = CampaignRef.from_dict(campaigns_item_data)

            campaigns.append(campaigns_item)

        can_call_out = d.pop("can_call_out")

        optout_line = d.pop("optout_line")

        number_usage = cls(
            campaigns=campaigns,
            can_call_out=can_call_out,
            optout_line=optout_line,
        )

        return number_usage
