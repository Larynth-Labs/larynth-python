from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatementLineParams")


@_attrs_define
class StatementLineParams:
    """
    Attributes:
        bundle_key (str | Unset):
        calls (int | Unset):
        e164 (str | Unset):
        numbers (int | Unset):
        payment_id (UUID | Unset):
        reason (str | Unset):
    """

    bundle_key: str | Unset = UNSET
    calls: int | Unset = UNSET
    e164: str | Unset = UNSET
    numbers: int | Unset = UNSET
    payment_id: UUID | Unset = UNSET
    reason: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        bundle_key = self.bundle_key

        calls = self.calls

        e164 = self.e164

        numbers = self.numbers

        payment_id: str | Unset = UNSET
        if not isinstance(self.payment_id, Unset):
            payment_id = str(self.payment_id)

        reason = self.reason

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if bundle_key is not UNSET:
            field_dict["bundle_key"] = bundle_key
        if calls is not UNSET:
            field_dict["calls"] = calls
        if e164 is not UNSET:
            field_dict["e164"] = e164
        if numbers is not UNSET:
            field_dict["numbers"] = numbers
        if payment_id is not UNSET:
            field_dict["payment_id"] = payment_id
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        bundle_key = d.pop("bundle_key", UNSET)

        calls = d.pop("calls", UNSET)

        e164 = d.pop("e164", UNSET)

        numbers = d.pop("numbers", UNSET)

        _payment_id = d.pop("payment_id", UNSET)
        payment_id: UUID | Unset
        if isinstance(_payment_id, Unset):
            payment_id = UNSET
        else:
            payment_id = UUID(_payment_id)

        reason = d.pop("reason", UNSET)

        statement_line_params = cls(
            bundle_key=bundle_key,
            calls=calls,
            e164=e164,
            numbers=numbers,
            payment_id=payment_id,
            reason=reason,
        )

        return statement_line_params
