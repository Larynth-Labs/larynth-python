from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..models.balance_currency import BalanceCurrency, check_balance_currency
from ..types import UNSET, Unset

T = TypeVar("T", bound="Balance")


@_attrs_define
class Balance:
    """
    Attributes:
        available_micro (int): Paid credit available
        bundle_credit_micro (int): Unused bundle credit; pays per-minute call charges only
        burn_micro_per_day_7d (int | None): Settled charges over the last 7 local days divided by 7; null below 3 active
            days
        currency (BalanceCurrency):
        held_micro (int): Reserved by calls in progress
        low_balance_threshold_micro (int):
        promo_credit_micro (int): Free credit (signup and promotions), spent before available funds on browser test and
            inbound calls
        total_credit_micro (int): available + promo + bundle credit
        updated_at (datetime.datetime):
        first_paid_at (datetime.datetime | Unset): First settled, risk-checked top-up or bundle payment
        runway_days (int | Unset): Days the total credit lasts at the 7-day burn; Owners and Admins only
    """

    available_micro: int
    bundle_credit_micro: int
    burn_micro_per_day_7d: int | None
    currency: BalanceCurrency
    held_micro: int
    low_balance_threshold_micro: int
    promo_credit_micro: int
    total_credit_micro: int
    updated_at: datetime.datetime
    first_paid_at: datetime.datetime | Unset = UNSET
    runway_days: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        available_micro = self.available_micro

        bundle_credit_micro = self.bundle_credit_micro

        burn_micro_per_day_7d: int | None
        burn_micro_per_day_7d = self.burn_micro_per_day_7d

        currency: str = self.currency

        held_micro = self.held_micro

        low_balance_threshold_micro = self.low_balance_threshold_micro

        promo_credit_micro = self.promo_credit_micro

        total_credit_micro = self.total_credit_micro

        updated_at = self.updated_at.isoformat()

        first_paid_at: str | Unset = UNSET
        if not isinstance(self.first_paid_at, Unset):
            first_paid_at = self.first_paid_at.isoformat()

        runway_days = self.runway_days

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "available_micro": available_micro,
                "bundle_credit_micro": bundle_credit_micro,
                "burn_micro_per_day_7d": burn_micro_per_day_7d,
                "currency": currency,
                "held_micro": held_micro,
                "low_balance_threshold_micro": low_balance_threshold_micro,
                "promo_credit_micro": promo_credit_micro,
                "total_credit_micro": total_credit_micro,
                "updated_at": updated_at,
            }
        )
        if first_paid_at is not UNSET:
            field_dict["first_paid_at"] = first_paid_at
        if runway_days is not UNSET:
            field_dict["runway_days"] = runway_days

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        available_micro = d.pop("available_micro")

        bundle_credit_micro = d.pop("bundle_credit_micro")

        def _parse_burn_micro_per_day_7d(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        burn_micro_per_day_7d = _parse_burn_micro_per_day_7d(
            d.pop("burn_micro_per_day_7d")
        )

        currency = check_balance_currency(d.pop("currency"))

        held_micro = d.pop("held_micro")

        low_balance_threshold_micro = d.pop("low_balance_threshold_micro")

        promo_credit_micro = d.pop("promo_credit_micro")

        total_credit_micro = d.pop("total_credit_micro")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _first_paid_at = d.pop("first_paid_at", UNSET)
        first_paid_at: datetime.datetime | Unset
        if isinstance(_first_paid_at, Unset):
            first_paid_at = UNSET
        else:
            first_paid_at = datetime.datetime.fromisoformat(_first_paid_at)

        runway_days = d.pop("runway_days", UNSET)

        balance = cls(
            available_micro=available_micro,
            bundle_credit_micro=bundle_credit_micro,
            burn_micro_per_day_7d=burn_micro_per_day_7d,
            currency=currency,
            held_micro=held_micro,
            low_balance_threshold_micro=low_balance_threshold_micro,
            promo_credit_micro=promo_credit_micro,
            total_credit_micro=total_credit_micro,
            updated_at=updated_at,
            first_paid_at=first_paid_at,
            runway_days=runway_days,
        )

        return balance
