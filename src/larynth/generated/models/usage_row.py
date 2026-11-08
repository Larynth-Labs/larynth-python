from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.usage_row_unit import UsageRowUnit, check_usage_row_unit
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
        quantity (int | Unset): Units billed: billed minutes, numbers renewed, branded calls or brand months; set with
            unit
        rate_micro (int | Unset): Price per unit when every line of the row has the same one; omitted when rates differ
        unit (UsageRowUnit | Unset): Billing unit of the row; omitted when the row mixes units
    """

    amount_micro: int
    billed_minutes: int
    calls: int
    key: str
    lines: UsageLines
    label: str | Unset = UNSET
    quantity: int | Unset = UNSET
    rate_micro: int | Unset = UNSET
    unit: UsageRowUnit | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        amount_micro = self.amount_micro

        billed_minutes = self.billed_minutes

        calls = self.calls

        key = self.key

        lines = self.lines.to_dict()

        label = self.label

        quantity = self.quantity

        rate_micro = self.rate_micro

        unit: str | Unset = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit

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
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if rate_micro is not UNSET:
            field_dict["rate_micro"] = rate_micro
        if unit is not UNSET:
            field_dict["unit"] = unit

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

        quantity = d.pop("quantity", UNSET)

        rate_micro = d.pop("rate_micro", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: UsageRowUnit | Unset
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = check_usage_row_unit(_unit)

        usage_row = cls(
            amount_micro=amount_micro,
            billed_minutes=billed_minutes,
            calls=calls,
            key=key,
            lines=lines,
            label=label,
            quantity=quantity,
            rate_micro=rate_micro,
            unit=unit,
        )

        return usage_row
