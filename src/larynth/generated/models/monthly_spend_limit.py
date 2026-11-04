from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MonthlySpendLimit")


@_attrs_define
class MonthlySpendLimit:
    """
    Attributes:
        alert_at_pct (list[int]):
        enabled (bool):
        resets_at (datetime.datetime):
        used_micro (int): Settled charges of every kind plus open holds this month
        budget_micro (int | Unset):
    """

    alert_at_pct: list[int]
    enabled: bool
    resets_at: datetime.datetime
    used_micro: int
    budget_micro: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        alert_at_pct = self.alert_at_pct

        enabled = self.enabled

        resets_at = self.resets_at.isoformat()

        used_micro = self.used_micro

        budget_micro = self.budget_micro

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "alert_at_pct": alert_at_pct,
                "enabled": enabled,
                "resets_at": resets_at,
                "used_micro": used_micro,
            }
        )
        if budget_micro is not UNSET:
            field_dict["budget_micro"] = budget_micro

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        alert_at_pct = cast(list[int], d.pop("alert_at_pct"))

        enabled = d.pop("enabled")

        resets_at = datetime.datetime.fromisoformat(d.pop("resets_at"))

        used_micro = d.pop("used_micro")

        budget_micro = d.pop("budget_micro", UNSET)

        monthly_spend_limit = cls(
            alert_at_pct=alert_at_pct,
            enabled=enabled,
            resets_at=resets_at,
            used_micro=used_micro,
            budget_micro=budget_micro,
        )

        return monthly_spend_limit
