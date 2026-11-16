from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="HumanRoute")


@_attrs_define
class HumanRoute:
    """
    Attributes:
        keypad_zero (bool | Unset): Pressing 0 on its own transfers the caller to the first transfer destination, with
            no model decision. Ignored while the agent collects a keypad entry. Unset is on
        spoken (bool | Unset): Saying person, human, representative, operator or agent transfers the caller to the first
            transfer destination, with no model decision. Unset is on
    """

    keypad_zero: bool | Unset = UNSET
    spoken: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        keypad_zero = self.keypad_zero

        spoken = self.spoken

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if keypad_zero is not UNSET:
            field_dict["keypad_zero"] = keypad_zero
        if spoken is not UNSET:
            field_dict["spoken"] = spoken

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        keypad_zero = d.pop("keypad_zero", UNSET)

        spoken = d.pop("spoken", UNSET)

        human_route = cls(
            keypad_zero=keypad_zero,
            spoken=spoken,
        )

        return human_route
