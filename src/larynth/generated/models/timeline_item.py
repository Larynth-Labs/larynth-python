from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.timeline_item_kind import TimelineItemKind, check_timeline_item_kind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.timeline_call import TimelineCall
    from ..models.timeline_campaign import TimelineCampaign
    from ..models.timeline_consent import TimelineConsent
    from ..models.timeline_item_params import TimelineItemParams


T = TypeVar("T", bound="TimelineItem")


@_attrs_define
class TimelineItem:
    """
    Attributes:
        at (datetime.datetime):
        id (str):
        kind (TimelineItemKind):
        call (TimelineCall | Unset):
        campaign (TimelineCampaign | Unset):
        consent (TimelineConsent | Unset):
        params (TimelineItemParams | Unset):
    """

    at: datetime.datetime
    id: str
    kind: TimelineItemKind
    call: TimelineCall | Unset = UNSET
    campaign: TimelineCampaign | Unset = UNSET
    consent: TimelineConsent | Unset = UNSET
    params: TimelineItemParams | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        at = self.at.isoformat()

        id = self.id

        kind: str = self.kind

        call: dict[str, Any] | Unset = UNSET
        if not isinstance(self.call, Unset):
            call = self.call.to_dict()

        campaign: dict[str, Any] | Unset = UNSET
        if not isinstance(self.campaign, Unset):
            campaign = self.campaign.to_dict()

        consent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.consent, Unset):
            consent = self.consent.to_dict()

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "at": at,
                "id": id,
                "kind": kind,
            }
        )
        if call is not UNSET:
            field_dict["call"] = call
        if campaign is not UNSET:
            field_dict["campaign"] = campaign
        if consent is not UNSET:
            field_dict["consent"] = consent
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.timeline_call import TimelineCall
        from ..models.timeline_campaign import TimelineCampaign
        from ..models.timeline_consent import TimelineConsent
        from ..models.timeline_item_params import TimelineItemParams

        d = dict(src_dict)
        at = datetime.datetime.fromisoformat(d.pop("at"))

        id = d.pop("id")

        kind = check_timeline_item_kind(d.pop("kind"))

        _call = d.pop("call", UNSET)
        call: TimelineCall | Unset
        if isinstance(_call, Unset):
            call = UNSET
        else:
            call = TimelineCall.from_dict(_call)

        _campaign = d.pop("campaign", UNSET)
        campaign: TimelineCampaign | Unset
        if isinstance(_campaign, Unset):
            campaign = UNSET
        else:
            campaign = TimelineCampaign.from_dict(_campaign)

        _consent = d.pop("consent", UNSET)
        consent: TimelineConsent | Unset
        if isinstance(_consent, Unset):
            consent = UNSET
        else:
            consent = TimelineConsent.from_dict(_consent)

        _params = d.pop("params", UNSET)
        params: TimelineItemParams | Unset
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = TimelineItemParams.from_dict(_params)

        timeline_item = cls(
            at=at,
            id=id,
            kind=kind,
            call=call,
            campaign=campaign,
            consent=consent,
            params=params,
        )

        return timeline_item
