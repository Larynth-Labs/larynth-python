from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.calls_not_billed import CallsNotBilled
    from ..models.calls_summary_by_outcome import CallsSummaryByOutcome
    from ..models.calls_summary_group import CallsSummaryGroup


T = TypeVar("T", bound="CallsSummary")


@_attrs_define
class CallsSummary:
    """
    Attributes:
        avg_billed_ms (int):
        billed_ms (int):
        by_outcome (CallsSummaryByOutcome):
        calls (int):
        connected (int):
        not_billed (CallsNotBilled):
        not_connected (int):
        rate_micro_per_min (int):
        spend_micro (int):
        groups (list[CallsSummaryGroup] | Unset):
    """

    avg_billed_ms: int
    billed_ms: int
    by_outcome: CallsSummaryByOutcome
    calls: int
    connected: int
    not_billed: CallsNotBilled
    not_connected: int
    rate_micro_per_min: int
    spend_micro: int
    groups: list[CallsSummaryGroup] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        avg_billed_ms = self.avg_billed_ms

        billed_ms = self.billed_ms

        by_outcome = self.by_outcome.to_dict()

        calls = self.calls

        connected = self.connected

        not_billed = self.not_billed.to_dict()

        not_connected = self.not_connected

        rate_micro_per_min = self.rate_micro_per_min

        spend_micro = self.spend_micro

        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "avg_billed_ms": avg_billed_ms,
                "billed_ms": billed_ms,
                "by_outcome": by_outcome,
                "calls": calls,
                "connected": connected,
                "not_billed": not_billed,
                "not_connected": not_connected,
                "rate_micro_per_min": rate_micro_per_min,
                "spend_micro": spend_micro,
            }
        )
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.calls_not_billed import CallsNotBilled
        from ..models.calls_summary_by_outcome import CallsSummaryByOutcome
        from ..models.calls_summary_group import CallsSummaryGroup

        d = dict(src_dict)
        avg_billed_ms = d.pop("avg_billed_ms")

        billed_ms = d.pop("billed_ms")

        by_outcome = CallsSummaryByOutcome.from_dict(d.pop("by_outcome"))

        calls = d.pop("calls")

        connected = d.pop("connected")

        not_billed = CallsNotBilled.from_dict(d.pop("not_billed"))

        not_connected = d.pop("not_connected")

        rate_micro_per_min = d.pop("rate_micro_per_min")

        spend_micro = d.pop("spend_micro")

        _groups = d.pop("groups", UNSET)
        groups: list[CallsSummaryGroup] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = CallsSummaryGroup.from_dict(groups_item_data)

                groups.append(groups_item)

        calls_summary = cls(
            avg_billed_ms=avg_billed_ms,
            billed_ms=billed_ms,
            by_outcome=by_outcome,
            calls=calls,
            connected=connected,
            not_billed=not_billed,
            not_connected=not_connected,
            rate_micro_per_min=rate_micro_per_min,
            spend_micro=spend_micro,
            groups=groups,
        )

        return calls_summary
