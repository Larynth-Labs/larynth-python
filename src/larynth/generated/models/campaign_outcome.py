from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.campaign_outcome_label import (
    CampaignOutcomeLabel,
    check_campaign_outcome_label,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CampaignOutcome")


@_attrs_define
class CampaignOutcome:
    """
    Attributes:
        count (int):
        outcome (str):
        label (CampaignOutcomeLabel | Unset):
    """

    count: int
    outcome: str
    label: CampaignOutcomeLabel | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        outcome = self.outcome

        label: str | Unset = UNSET
        if not isinstance(self.label, Unset):
            label = self.label

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
                "outcome": outcome,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        count = d.pop("count")

        outcome = d.pop("outcome")

        _label = d.pop("label", UNSET)
        label: CampaignOutcomeLabel | Unset
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = check_campaign_outcome_label(_label)

        campaign_outcome = cls(
            count=count,
            outcome=outcome,
            label=label,
        )

        return campaign_outcome
