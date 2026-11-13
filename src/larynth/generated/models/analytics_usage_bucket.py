from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AnalyticsUsageBucket")


@_attrs_define
class AnalyticsUsageBucket:
    """
    Attributes:
        billed_minutes (int):
        calls (int):
        spend_micro (int): Charges written to the ledger, micro-USD
    """

    billed_minutes: int
    calls: int
    spend_micro: int

    def to_dict(self) -> dict[str, Any]:
        billed_minutes = self.billed_minutes

        calls = self.calls

        spend_micro = self.spend_micro

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "billed_minutes": billed_minutes,
                "calls": calls,
                "spend_micro": spend_micro,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        billed_minutes = d.pop("billed_minutes")

        calls = d.pop("calls")

        spend_micro = d.pop("spend_micro")

        analytics_usage_bucket = cls(
            billed_minutes=billed_minutes,
            calls=calls,
            spend_micro=spend_micro,
        )

        return analytics_usage_bucket
