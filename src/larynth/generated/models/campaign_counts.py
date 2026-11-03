from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.campaign_counts_by_display_status import CampaignCountsByDisplayStatus


T = TypeVar("T", bound="CampaignCounts")


@_attrs_define
class CampaignCounts:
    """
    Attributes:
        by_display_status (CampaignCountsByDisplayStatus):
    """

    by_display_status: CampaignCountsByDisplayStatus

    def to_dict(self) -> dict[str, Any]:
        by_display_status = self.by_display_status.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "by_display_status": by_display_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.campaign_counts_by_display_status import (
            CampaignCountsByDisplayStatus,
        )

        d = dict(src_dict)
        by_display_status = CampaignCountsByDisplayStatus.from_dict(
            d.pop("by_display_status")
        )

        campaign_counts = cls(
            by_display_status=by_display_status,
        )

        return campaign_counts
