from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.campaign_progress_by_state import CampaignProgressByState


T = TypeVar("T", bound="CampaignProgress")


@_attrs_define
class CampaignProgress:
    """
    Attributes:
        by_state (CampaignProgressByState):
        contacts_total (int):
        reached (int):
    """

    by_state: CampaignProgressByState
    contacts_total: int
    reached: int

    def to_dict(self) -> dict[str, Any]:
        by_state = self.by_state.to_dict()

        contacts_total = self.contacts_total

        reached = self.reached

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "by_state": by_state,
                "contacts_total": contacts_total,
                "reached": reached,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.campaign_progress_by_state import CampaignProgressByState

        d = dict(src_dict)
        by_state = CampaignProgressByState.from_dict(d.pop("by_state"))

        contacts_total = d.pop("contacts_total")

        reached = d.pop("reached")

        campaign_progress = cls(
            by_state=by_state,
            contacts_total=contacts_total,
            reached=reached,
        )

        return campaign_progress
