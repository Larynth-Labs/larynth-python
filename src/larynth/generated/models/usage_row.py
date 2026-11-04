from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usage_lines import UsageLines


T = TypeVar("T", bound="UsageRow")


@_attrs_define
class UsageRow:
    """
    Attributes:
        amount_micro (int):
        billed_minutes (int):
        calls (int):
        key (str): Category, agent id, local date or number id
        lines (UsageLines):
        label (str | Unset): Agent name (last name of deleted agents) or number
    """

    amount_micro: int
    billed_minutes: int
    calls: int
    key: str
    lines: UsageLines
    label: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        amount_micro = self.amount_micro

        billed_minutes = self.billed_minutes

        calls = self.calls

        key = self.key

        lines = self.lines.to_dict()

        label = self.label

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount_micro": amount_micro,
                "billed_minutes": billed_minutes,
                "calls": calls,
                "key": key,
                "lines": lines,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.usage_lines import UsageLines

        d = dict(src_dict)
        amount_micro = d.pop("amount_micro")

        billed_minutes = d.pop("billed_minutes")

        calls = d.pop("calls")

        key = d.pop("key")

        lines = UsageLines.from_dict(d.pop("lines"))

        label = d.pop("label", UNSET)

        usage_row = cls(
            amount_micro=amount_micro,
            billed_minutes=billed_minutes,
            calls=calls,
            key=key,
            lines=lines,
            label=label,
        )

        return usage_row
