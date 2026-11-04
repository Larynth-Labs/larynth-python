from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DailySpendLimit")


@_attrs_define
class DailySpendLimit:
    """
    Attributes:
        alert_at_pct (list[int]):
        enabled (bool):
        resets_at (datetime.datetime): Next midnight in the workspace time zone
        used_micro (int): Settled charges of every kind plus open holds today
        cap_micro (int | Unset):
    """

    alert_at_pct: list[int]
    enabled: bool
    resets_at: datetime.datetime
    used_micro: int
    cap_micro: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        alert_at_pct = self.alert_at_pct

        enabled = self.enabled

        resets_at = self.resets_at.isoformat()

        used_micro = self.used_micro

        cap_micro = self.cap_micro

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "alert_at_pct": alert_at_pct,
                "enabled": enabled,
                "resets_at": resets_at,
                "used_micro": used_micro,
            }
        )
        if cap_micro is not UNSET:
            field_dict["cap_micro"] = cap_micro

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        alert_at_pct = cast(list[int], d.pop("alert_at_pct"))

        enabled = d.pop("enabled")

        resets_at = datetime.datetime.fromisoformat(d.pop("resets_at"))

        used_micro = d.pop("used_micro")

        cap_micro = d.pop("cap_micro", UNSET)

        daily_spend_limit = cls(
            alert_at_pct=alert_at_pct,
            enabled=enabled,
            resets_at=resets_at,
            used_micro=used_micro,
            cap_micro=cap_micro,
        )

        return daily_spend_limit
