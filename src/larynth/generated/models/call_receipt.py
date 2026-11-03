from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.call_receipt_not_billed_reason import (
    CallReceiptNotBilledReason,
    check_call_receipt_not_billed_reason,
)
from ..models.call_receipt_rounding import (
    CallReceiptRounding,
    check_call_receipt_rounding,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.call_receipt_line import CallReceiptLine


T = TypeVar("T", bound="CallReceipt")


@_attrs_define
class CallReceipt:
    """
    Attributes:
        free_under_ms (int):
        lines (list[CallReceiptLine]):
        rounding (CallReceiptRounding):
        total_micro (int):
        ledger_transaction_id (UUID | Unset):
        not_billed_reason (CallReceiptNotBilledReason | Unset):
        settled_at (datetime.datetime | Unset):
    """

    free_under_ms: int
    lines: list[CallReceiptLine]
    rounding: CallReceiptRounding
    total_micro: int
    ledger_transaction_id: UUID | Unset = UNSET
    not_billed_reason: CallReceiptNotBilledReason | Unset = UNSET
    settled_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        free_under_ms = self.free_under_ms

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        rounding: str = self.rounding

        total_micro = self.total_micro

        ledger_transaction_id: str | Unset = UNSET
        if not isinstance(self.ledger_transaction_id, Unset):
            ledger_transaction_id = str(self.ledger_transaction_id)

        not_billed_reason: str | Unset = UNSET
        if not isinstance(self.not_billed_reason, Unset):
            not_billed_reason = self.not_billed_reason

        settled_at: str | Unset = UNSET
        if not isinstance(self.settled_at, Unset):
            settled_at = self.settled_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "free_under_ms": free_under_ms,
                "lines": lines,
                "rounding": rounding,
                "total_micro": total_micro,
            }
        )
        if ledger_transaction_id is not UNSET:
            field_dict["ledger_transaction_id"] = ledger_transaction_id
        if not_billed_reason is not UNSET:
            field_dict["not_billed_reason"] = not_billed_reason
        if settled_at is not UNSET:
            field_dict["settled_at"] = settled_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.call_receipt_line import CallReceiptLine

        d = dict(src_dict)
        free_under_ms = d.pop("free_under_ms")

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = CallReceiptLine.from_dict(lines_item_data)

            lines.append(lines_item)

        rounding = check_call_receipt_rounding(d.pop("rounding"))

        total_micro = d.pop("total_micro")

        _ledger_transaction_id = d.pop("ledger_transaction_id", UNSET)
        ledger_transaction_id: UUID | Unset
        if isinstance(_ledger_transaction_id, Unset):
            ledger_transaction_id = UNSET
        else:
            ledger_transaction_id = UUID(_ledger_transaction_id)

        _not_billed_reason = d.pop("not_billed_reason", UNSET)
        not_billed_reason: CallReceiptNotBilledReason | Unset
        if isinstance(_not_billed_reason, Unset):
            not_billed_reason = UNSET
        else:
            not_billed_reason = check_call_receipt_not_billed_reason(_not_billed_reason)

        _settled_at = d.pop("settled_at", UNSET)
        settled_at: datetime.datetime | Unset
        if isinstance(_settled_at, Unset):
            settled_at = UNSET
        else:
            settled_at = datetime.datetime.fromisoformat(_settled_at)

        call_receipt = cls(
            free_under_ms=free_under_ms,
            lines=lines,
            rounding=rounding,
            total_micro=total_micro,
            ledger_transaction_id=ledger_transaction_id,
            not_billed_reason=not_billed_reason,
            settled_at=settled_at,
        )

        return call_receipt
