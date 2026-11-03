from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="StateAudience")


@_attrs_define
class StateAudience:
    """
    Attributes:
        count (int):
        rule_notes (list[str]):
        state (str):
    """

    count: int
    rule_notes: list[str]
    state: str

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        rule_notes = self.rule_notes

        state = self.state

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
                "rule_notes": rule_notes,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        count = d.pop("count")

        rule_notes = cast(list[str], d.pop("rule_notes"))

        state = d.pop("state")

        state_audience = cls(
            count=count,
            rule_notes=rule_notes,
            state=state,
        )

        return state_audience
