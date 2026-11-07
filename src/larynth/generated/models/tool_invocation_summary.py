from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.tool_invocation_summary_outcome import (
    ToolInvocationSummaryOutcome,
    check_tool_invocation_summary_outcome,
)

T = TypeVar("T", bound="ToolInvocationSummary")


@_attrs_define
class ToolInvocationSummary:
    """
    Attributes:
        at (datetime.datetime):
        outcome (ToolInvocationSummaryOutcome):
        took_ms (int):
    """

    at: datetime.datetime
    outcome: ToolInvocationSummaryOutcome
    took_ms: int

    def to_dict(self) -> dict[str, Any]:
        at = self.at.isoformat()

        outcome: str = self.outcome

        took_ms = self.took_ms

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "at": at,
                "outcome": outcome,
                "took_ms": took_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        at = datetime.datetime.fromisoformat(d.pop("at"))

        outcome = check_tool_invocation_summary_outcome(d.pop("outcome"))

        took_ms = d.pop("took_ms")

        tool_invocation_summary = cls(
            at=at,
            outcome=outcome,
            took_ms=took_ms,
        )

        return tool_invocation_summary
