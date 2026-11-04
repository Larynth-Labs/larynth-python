from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.campaign_ref_status import CampaignRefStatus, check_campaign_ref_status

T = TypeVar("T", bound="CampaignRef")


@_attrs_define
class CampaignRef:
    """
    Attributes:
        id (UUID):
        name (str):
        status (CampaignRefStatus):
    """

    id: UUID
    name: str
    status: CampaignRefStatus

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        status: str = self.status

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        status = check_campaign_ref_status(d.pop("status"))

        campaign_ref = cls(
            id=id,
            name=name,
            status=status,
        )

        return campaign_ref
