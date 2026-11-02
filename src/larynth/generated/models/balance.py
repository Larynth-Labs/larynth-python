from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.balance_currency import BalanceCurrency, check_balance_currency

T = TypeVar("T", bound="Balance")


@_attrs_define
class Balance:
    """
    Attributes:
        available_micro (int):
        currency (BalanceCurrency):
        held_micro (int): Reserved by calls in progress
        low_balance_threshold_micro (int):
        promo_credit_micro (int): Free credit (signup and promotions), spent before available funds
        updated_at (datetime.datetime):
    """

    available_micro: int
    currency: BalanceCurrency
    held_micro: int
    low_balance_threshold_micro: int
    promo_credit_micro: int
    updated_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        available_micro = self.available_micro

        currency: str = self.currency

        held_micro = self.held_micro

        low_balance_threshold_micro = self.low_balance_threshold_micro

        promo_credit_micro = self.promo_credit_micro

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "available_micro": available_micro,
                "currency": currency,
                "held_micro": held_micro,
                "low_balance_threshold_micro": low_balance_threshold_micro,
                "promo_credit_micro": promo_credit_micro,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        available_micro = d.pop("available_micro")

        currency = check_balance_currency(d.pop("currency"))

        held_micro = d.pop("held_micro")

        low_balance_threshold_micro = d.pop("low_balance_threshold_micro")

        promo_credit_micro = d.pop("promo_credit_micro")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        balance = cls(
            available_micro=available_micro,
            currency=currency,
            held_micro=held_micro,
            low_balance_threshold_micro=low_balance_threshold_micro,
            promo_credit_micro=promo_credit_micro,
            updated_at=updated_at,
        )

        return balance
