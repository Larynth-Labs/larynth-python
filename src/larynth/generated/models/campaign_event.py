from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.campaign_event_kind import CampaignEventKind, check_campaign_event_kind
from ..models.campaign_event_tone import CampaignEventTone, check_campaign_event_tone
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.campaign_event_params import CampaignEventParams


T = TypeVar("T", bound="CampaignEvent")


@_attrs_define
class CampaignEvent:
    """
    Attributes:
        at (datetime.datetime):
        count (int): Events of this kind rolled into the hour
        id (UUID):
        kind (CampaignEventKind):
        tone (CampaignEventTone):
        params (CampaignEventParams | Unset):
    """

    at: datetime.datetime
    count: int
    id: UUID
    kind: CampaignEventKind
    tone: CampaignEventTone
    params: CampaignEventParams | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        at = self.at.isoformat()

        count = self.count

        id = str(self.id)

        kind: str = self.kind

        tone: str = self.tone

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "at": at,
                "count": count,
                "id": id,
                "kind": kind,
                "tone": tone,
            }
        )
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.campaign_event_params import CampaignEventParams

        d = dict(src_dict)
        at = datetime.datetime.fromisoformat(d.pop("at"))

        count = d.pop("count")

        id = UUID(d.pop("id"))

        kind = check_campaign_event_kind(d.pop("kind"))

        tone = check_campaign_event_tone(d.pop("tone"))

        _params = d.pop("params", UNSET)
        params: CampaignEventParams | Unset
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = CampaignEventParams.from_dict(_params)

        campaign_event = cls(
            at=at,
            count=count,
            id=id,
            kind=kind,
            tone=tone,
            params=params,
        )

        return campaign_event
