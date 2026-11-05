from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.call_receipt_line_kind import (
    CallReceiptLineKind,
    check_call_receipt_line_kind,
)
from ..types import UNSET, Unset

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
        bundle_funded_micro (int | Unset): Part of amount_micro paid from bundle credit
        display_name (str | Unset): Catalog name of the premium voice or model; only on premium lines
        launch_price (bool | Unset): The workspace's launch price applied to this line
        list_price_micro (int | Unset): Per-minute list price the launch price replaced; only with launch_price
    """

    amount_micro: int
    billed_minutes: int
    kind: CallReceiptLineKind
    quantity_ms: int
    unit_price_micro: int
    bundle_funded_micro: int | Unset = UNSET
    display_name: str | Unset = UNSET
    launch_price: bool | Unset = UNSET
    list_price_micro: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        amount_micro = self.amount_micro

        billed_minutes = self.billed_minutes

        kind: str = self.kind

        quantity_ms = self.quantity_ms

        unit_price_micro = self.unit_price_micro

        bundle_funded_micro = self.bundle_funded_micro

        display_name = self.display_name

        launch_price = self.launch_price

        list_price_micro = self.list_price_micro

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
        if bundle_funded_micro is not UNSET:
            field_dict["bundle_funded_micro"] = bundle_funded_micro
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if launch_price is not UNSET:
            field_dict["launch_price"] = launch_price
        if list_price_micro is not UNSET:
            field_dict["list_price_micro"] = list_price_micro

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount_micro = d.pop("amount_micro")

        billed_minutes = d.pop("billed_minutes")

        kind = check_call_receipt_line_kind(d.pop("kind"))

        quantity_ms = d.pop("quantity_ms")

        unit_price_micro = d.pop("unit_price_micro")

        bundle_funded_micro = d.pop("bundle_funded_micro", UNSET)

        display_name = d.pop("display_name", UNSET)

        launch_price = d.pop("launch_price", UNSET)

        list_price_micro = d.pop("list_price_micro", UNSET)

        call_receipt_line = cls(
            amount_micro=amount_micro,
            billed_minutes=billed_minutes,
            kind=kind,
            quantity_ms=quantity_ms,
            unit_price_micro=unit_price_micro,
            bundle_funded_micro=bundle_funded_micro,
            display_name=display_name,
            launch_price=launch_price,
            list_price_micro=list_price_micro,
        )

        return call_receipt_line
