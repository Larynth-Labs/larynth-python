from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.timeline_call_direction import (
    TimelineCallDirection,
    check_timeline_call_direction,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TimelineCall")


@_attrs_define
class TimelineCall:
    """
    Attributes:
        call_id (str):
        direction (TimelineCallDirection):
        duration_ms (int):
        assistant_name (str | Unset):
        campaign_id (UUID | Unset):
        outcome (str | Unset):
        price_micro (int | Unset):
        summary (str | Unset): Follows transcript retention
    """

    call_id: str
    direction: TimelineCallDirection
    duration_ms: int
    assistant_name: str | Unset = UNSET
    campaign_id: UUID | Unset = UNSET
    outcome: str | Unset = UNSET
    price_micro: int | Unset = UNSET
    summary: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        call_id = self.call_id

        direction: str = self.direction

        duration_ms = self.duration_ms

        assistant_name = self.assistant_name

        campaign_id: str | Unset = UNSET
        if not isinstance(self.campaign_id, Unset):
            campaign_id = str(self.campaign_id)

        outcome = self.outcome

        price_micro = self.price_micro

        summary = self.summary

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "call_id": call_id,
                "direction": direction,
                "duration_ms": duration_ms,
            }
        )
        if assistant_name is not UNSET:
            field_dict["assistant_name"] = assistant_name
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if price_micro is not UNSET:
            field_dict["price_micro"] = price_micro
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        call_id = d.pop("call_id")

        direction = check_timeline_call_direction(d.pop("direction"))

        duration_ms = d.pop("duration_ms")

        assistant_name = d.pop("assistant_name", UNSET)

        _campaign_id = d.pop("campaign_id", UNSET)
        campaign_id: UUID | Unset
        if isinstance(_campaign_id, Unset):
            campaign_id = UNSET
        else:
            campaign_id = UUID(_campaign_id)

        outcome = d.pop("outcome", UNSET)

        price_micro = d.pop("price_micro", UNSET)

        summary = d.pop("summary", UNSET)

        timeline_call = cls(
            call_id=call_id,
            direction=direction,
            duration_ms=duration_ms,
            assistant_name=assistant_name,
            campaign_id=campaign_id,
            outcome=outcome,
            price_micro=price_micro,
            summary=summary,
        )

        return timeline_call
