from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.campaign_safeguard_reason import (
    CampaignSafeguardReason,
    check_campaign_safeguard_reason,
)
from ..models.campaign_safeguard_state import (
    CampaignSafeguardState,
    check_campaign_safeguard_state,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.campaign_safeguard_metric import CampaignSafeguardMetric
    from ..models.campaign_safeguard_threshold import CampaignSafeguardThreshold


T = TypeVar("T", bound="CampaignSafeguard")


@_attrs_define
class CampaignSafeguard:
    """
    Attributes:
        metric (CampaignSafeguardMetric):
        paused_at (datetime.datetime):
        reason (CampaignSafeguardReason):
        state (CampaignSafeguardState):
        threshold (CampaignSafeguardThreshold):
        decided_at (datetime.datetime | Unset):
        note (str | Unset): Larynth reviewer's note
        requested_at (datetime.datetime | Unset):
    """

    metric: CampaignSafeguardMetric
    paused_at: datetime.datetime
    reason: CampaignSafeguardReason
    state: CampaignSafeguardState
    threshold: CampaignSafeguardThreshold
    decided_at: datetime.datetime | Unset = UNSET
    note: str | Unset = UNSET
    requested_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        metric = self.metric.to_dict()

        paused_at = self.paused_at.isoformat()

        reason: str = self.reason

        state: str = self.state

        threshold = self.threshold.to_dict()

        decided_at: str | Unset = UNSET
        if not isinstance(self.decided_at, Unset):
            decided_at = self.decided_at.isoformat()

        note = self.note

        requested_at: str | Unset = UNSET
        if not isinstance(self.requested_at, Unset):
            requested_at = self.requested_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "metric": metric,
                "paused_at": paused_at,
                "reason": reason,
                "state": state,
                "threshold": threshold,
            }
        )
        if decided_at is not UNSET:
            field_dict["decided_at"] = decided_at
        if note is not UNSET:
            field_dict["note"] = note
        if requested_at is not UNSET:
            field_dict["requested_at"] = requested_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.campaign_safeguard_metric import CampaignSafeguardMetric
        from ..models.campaign_safeguard_threshold import CampaignSafeguardThreshold

        d = dict(src_dict)
        metric = CampaignSafeguardMetric.from_dict(d.pop("metric"))

        paused_at = datetime.datetime.fromisoformat(d.pop("paused_at"))

        reason = check_campaign_safeguard_reason(d.pop("reason"))

        state = check_campaign_safeguard_state(d.pop("state"))

        threshold = CampaignSafeguardThreshold.from_dict(d.pop("threshold"))

        _decided_at = d.pop("decided_at", UNSET)
        decided_at: datetime.datetime | Unset
        if isinstance(_decided_at, Unset):
            decided_at = UNSET
        else:
            decided_at = datetime.datetime.fromisoformat(_decided_at)

        note = d.pop("note", UNSET)

        _requested_at = d.pop("requested_at", UNSET)
        requested_at: datetime.datetime | Unset
        if isinstance(_requested_at, Unset):
            requested_at = UNSET
        else:
            requested_at = datetime.datetime.fromisoformat(_requested_at)

        campaign_safeguard = cls(
            metric=metric,
            paused_at=paused_at,
            reason=reason,
            state=state,
            threshold=threshold,
            decided_at=decided_at,
            note=note,
            requested_at=requested_at,
        )

        return campaign_safeguard
