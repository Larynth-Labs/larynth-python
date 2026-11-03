from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CallLimits")


@_attrs_define
class CallLimits:
    """
    Attributes:
        hold_max_s (int): Most time spent on hold after a phone menu on one call
        max_menu_cost_micro (int): Most a call can spend in menus and on hold at this agent's per-minute price, in
            micro-units of the account currency
        micro_per_minute (int):
        phone_menu_max_s (int): Most time spent in phone menus on one call
    """

    hold_max_s: int
    max_menu_cost_micro: int
    micro_per_minute: int
    phone_menu_max_s: int

    def to_dict(self) -> dict[str, Any]:
        hold_max_s = self.hold_max_s

        max_menu_cost_micro = self.max_menu_cost_micro

        micro_per_minute = self.micro_per_minute

        phone_menu_max_s = self.phone_menu_max_s

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "hold_max_s": hold_max_s,
                "max_menu_cost_micro": max_menu_cost_micro,
                "micro_per_minute": micro_per_minute,
                "phone_menu_max_s": phone_menu_max_s,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        hold_max_s = d.pop("hold_max_s")

        max_menu_cost_micro = d.pop("max_menu_cost_micro")

        micro_per_minute = d.pop("micro_per_minute")

        phone_menu_max_s = d.pop("phone_menu_max_s")

        call_limits = cls(
            hold_max_s=hold_max_s,
            max_menu_cost_micro=max_menu_cost_micro,
            micro_per_minute=micro_per_minute,
            phone_menu_max_s=phone_menu_max_s,
        )

        return call_limits
