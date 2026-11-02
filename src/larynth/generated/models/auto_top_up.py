from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="AutoTopUp")


@_attrs_define
class AutoTopUp:
    """
    Attributes:
        amount_micro (int):
        enabled (bool):
        has_payment_method (bool):
        low_balance_threshold_micro (int):
        threshold_micro (int):
        updated_at (datetime.datetime):
    """

    amount_micro: int
    enabled: bool
    has_payment_method: bool
    low_balance_threshold_micro: int
    threshold_micro: int
    updated_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        amount_micro = self.amount_micro

        enabled = self.enabled

        has_payment_method = self.has_payment_method

        low_balance_threshold_micro = self.low_balance_threshold_micro

        threshold_micro = self.threshold_micro

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount_micro": amount_micro,
                "enabled": enabled,
                "has_payment_method": has_payment_method,
                "low_balance_threshold_micro": low_balance_threshold_micro,
                "threshold_micro": threshold_micro,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount_micro = d.pop("amount_micro")

        enabled = d.pop("enabled")

        has_payment_method = d.pop("has_payment_method")

        low_balance_threshold_micro = d.pop("low_balance_threshold_micro")

        threshold_micro = d.pop("threshold_micro")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        auto_top_up = cls(
            amount_micro=amount_micro,
            enabled=enabled,
            has_payment_method=has_payment_method,
            low_balance_threshold_micro=low_balance_threshold_micro,
            threshold_micro=threshold_micro,
            updated_at=updated_at,
        )

        return auto_top_up
