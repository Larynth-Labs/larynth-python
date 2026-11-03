from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.call_receipt_line_kind import (
    CallReceiptLineKind,
    check_call_receipt_line_kind,
)

T = TypeVar("T", bound="CallReceiptLine")


@_attrs_define
class CallReceiptLine:
    """
    Attributes:
        amount_micro (int):
        billed_minutes (int):
        kind (CallReceiptLineKind):
        quantity_ms (int):
        unit_price_micro (int):
    """

    amount_micro: int
    billed_minutes: int
    kind: CallReceiptLineKind
    quantity_ms: int
    unit_price_micro: int

    def to_dict(self) -> dict[str, Any]:
        amount_micro = self.amount_micro

        billed_minutes = self.billed_minutes

        kind: str = self.kind

        quantity_ms = self.quantity_ms

        unit_price_micro = self.unit_price_micro

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount_micro": amount_micro,
                "billed_minutes": billed_minutes,
                "kind": kind,
                "quantity_ms": quantity_ms,
                "unit_price_micro": unit_price_micro,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount_micro = d.pop("amount_micro")

        billed_minutes = d.pop("billed_minutes")

        kind = check_call_receipt_line_kind(d.pop("kind"))

        quantity_ms = d.pop("quantity_ms")

        unit_price_micro = d.pop("unit_price_micro")

        call_receipt_line = cls(
            amount_micro=amount_micro,
            billed_minutes=billed_minutes,
            kind=kind,
            quantity_ms=quantity_ms,
            unit_price_micro=unit_price_micro,
        )

        return call_receipt_line
