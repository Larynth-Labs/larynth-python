from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AutoTopUp")


@_attrs_define
class AutoTopUp:
    """
    Attributes:
        amount_micro (int):
        available (bool): Always false: auto top-up is off and customers top up through checkout
        enabled (bool): Always false: auto top-up is off
        has_payment_method (bool):
        low_balance_threshold_micro (int):
        threshold_micro (int):
        updated_at (datetime.datetime):
        payment_method_id (str | Unset): Card auto top-up charges; the default card when empty
    """

    amount_micro: int
    available: bool
    enabled: bool
    has_payment_method: bool
    low_balance_threshold_micro: int
    threshold_micro: int
    updated_at: datetime.datetime
    payment_method_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        amount_micro = self.amount_micro

        available = self.available

        enabled = self.enabled

        has_payment_method = self.has_payment_method

        low_balance_threshold_micro = self.low_balance_threshold_micro

        threshold_micro = self.threshold_micro

        updated_at = self.updated_at.isoformat()

        payment_method_id = self.payment_method_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount_micro": amount_micro,
                "available": available,
                "enabled": enabled,
                "has_payment_method": has_payment_method,
                "low_balance_threshold_micro": low_balance_threshold_micro,
                "threshold_micro": threshold_micro,
                "updated_at": updated_at,
            }
        )
        if payment_method_id is not UNSET:
            field_dict["payment_method_id"] = payment_method_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount_micro = d.pop("amount_micro")

        available = d.pop("available")

        enabled = d.pop("enabled")

        has_payment_method = d.pop("has_payment_method")

        low_balance_threshold_micro = d.pop("low_balance_threshold_micro")

        threshold_micro = d.pop("threshold_micro")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        payment_method_id = d.pop("payment_method_id", UNSET)

        auto_top_up = cls(
            amount_micro=amount_micro,
            available=available,
            enabled=enabled,
            has_payment_method=has_payment_method,
            low_balance_threshold_micro=low_balance_threshold_micro,
            threshold_micro=threshold_micro,
            updated_at=updated_at,
            payment_method_id=payment_method_id,
        )

        return auto_top_up
