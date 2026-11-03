from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.campaign_outcome import CampaignOutcome
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
        abandonment_rate_30d (float | Unset):
        answer_rate (float | Unset):
        optout_rate (float | Unset):
        outcomes (list[CampaignOutcome] | Unset):
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
    abandonment_rate_30d: float | Unset = UNSET
    answer_rate: float | Unset = UNSET
    optout_rate: float | Unset = UNSET
    outcomes: list[CampaignOutcome] | Unset = UNSET

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

        abandonment_rate_30d = self.abandonment_rate_30d

        answer_rate = self.answer_rate

        optout_rate = self.optout_rate

        outcomes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.outcomes, Unset):
            outcomes = []
            for outcomes_item_data in self.outcomes:
                outcomes_item = outcomes_item_data.to_dict()
                outcomes.append(outcomes_item)

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
        if abandonment_rate_30d is not UNSET:
            field_dict["abandonment_rate_30d"] = abandonment_rate_30d
        if answer_rate is not UNSET:
            field_dict["answer_rate"] = answer_rate
        if optout_rate is not UNSET:
            field_dict["optout_rate"] = optout_rate
        if outcomes is not UNSET:
            field_dict["outcomes"] = outcomes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.campaign_outcome import CampaignOutcome
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

        abandonment_rate_30d = d.pop("abandonment_rate_30d", UNSET)

        answer_rate = d.pop("answer_rate", UNSET)

        optout_rate = d.pop("optout_rate", UNSET)

        _outcomes = d.pop("outcomes", UNSET)
        outcomes: list[CampaignOutcome] | Unset = UNSET
        if _outcomes is not UNSET:
            outcomes = []
            for outcomes_item_data in _outcomes:
                outcomes_item = CampaignOutcome.from_dict(outcomes_item_data)

                outcomes.append(outcomes_item)

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
            abandonment_rate_30d=abandonment_rate_30d,
            answer_rate=answer_rate,
            optout_rate=optout_rate,
            outcomes=outcomes,
        )

        return campaign_stats
