from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.campaign_stats_by_state import CampaignStatsByState


T = TypeVar("T", bound="CampaignStats")


@_attrs_define
class CampaignStats:
    """
    Attributes:
        answered (int):
        as_of (datetime.datetime):
        by_state (CampaignStatsByState):
        calls_active (int):
        calls_total (int):
        campaign_id (UUID):
        contacts_total (int):
        human (int):
        machine (int):
        opted_out (int):
        spent_micro (int):
    """

    answered: int
    as_of: datetime.datetime
    by_state: CampaignStatsByState
    calls_active: int
    calls_total: int
    campaign_id: UUID
    contacts_total: int
    human: int
    machine: int
    opted_out: int
    spent_micro: int

    def to_dict(self) -> dict[str, Any]:
        answered = self.answered

        as_of = self.as_of.isoformat()

        by_state = self.by_state.to_dict()

        calls_active = self.calls_active

        calls_total = self.calls_total

        campaign_id = str(self.campaign_id)

        contacts_total = self.contacts_total

        human = self.human

        machine = self.machine

        opted_out = self.opted_out

        spent_micro = self.spent_micro

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "answered": answered,
                "as_of": as_of,
                "by_state": by_state,
                "calls_active": calls_active,
                "calls_total": calls_total,
                "campaign_id": campaign_id,
                "contacts_total": contacts_total,
                "human": human,
                "machine": machine,
                "opted_out": opted_out,
                "spent_micro": spent_micro,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.campaign_stats_by_state import CampaignStatsByState

        d = dict(src_dict)
        answered = d.pop("answered")

        as_of = datetime.datetime.fromisoformat(d.pop("as_of"))

        by_state = CampaignStatsByState.from_dict(d.pop("by_state"))

        calls_active = d.pop("calls_active")

        calls_total = d.pop("calls_total")

        campaign_id = UUID(d.pop("campaign_id"))

        contacts_total = d.pop("contacts_total")

        human = d.pop("human")

        machine = d.pop("machine")

        opted_out = d.pop("opted_out")

        spent_micro = d.pop("spent_micro")

        campaign_stats = cls(
            answered=answered,
            as_of=as_of,
            by_state=by_state,
            calls_active=calls_active,
            calls_total=calls_total,
            campaign_id=campaign_id,
            contacts_total=contacts_total,
            human=human,
            machine=machine,
            opted_out=opted_out,
            spent_micro=spent_micro,
        )

        return campaign_stats
