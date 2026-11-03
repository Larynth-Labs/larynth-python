from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_campaign_request import CreateCampaignRequest


T = TypeVar("T", bound="EstimateCampaignRequest")


@_attrs_define
class EstimateCampaignRequest:
    """
    Attributes:
        campaign_id (UUID | Unset):
        draft (CreateCampaignRequest | Unset):
    """

    campaign_id: UUID | Unset = UNSET
    draft: CreateCampaignRequest | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        campaign_id: str | Unset = UNSET
        if not isinstance(self.campaign_id, Unset):
            campaign_id = str(self.campaign_id)

        draft: dict[str, Any] | Unset = UNSET
        if not isinstance(self.draft, Unset):
            draft = self.draft.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if draft is not UNSET:
            field_dict["draft"] = draft

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_campaign_request import CreateCampaignRequest

        d = dict(src_dict)
        _campaign_id = d.pop("campaign_id", UNSET)
        campaign_id: UUID | Unset
        if isinstance(_campaign_id, Unset):
            campaign_id = UNSET
        else:
            campaign_id = UUID(_campaign_id)

        _draft = d.pop("draft", UNSET)
        draft: CreateCampaignRequest | Unset
        if isinstance(_draft, Unset):
            draft = UNSET
        else:
            draft = CreateCampaignRequest.from_dict(_draft)

        estimate_campaign_request = cls(
            campaign_id=campaign_id,
            draft=draft,
        )

        return estimate_campaign_request
