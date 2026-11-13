from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AnalyticsOutcomeCount")


@_attrs_define
class AnalyticsOutcomeCount:
    """
    Attributes:
        calls (int):
        outcome (str): Call outcome; unknown while a call has none
    """

    calls: int
    outcome: str

    def to_dict(self) -> dict[str, Any]:
        calls = self.calls

        outcome = self.outcome

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "calls": calls,
                "outcome": outcome,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        calls = d.pop("calls")

        outcome = d.pop("outcome")

        analytics_outcome_count = cls(
            calls=calls,
            outcome=outcome,
        )

        return analytics_outcome_count
