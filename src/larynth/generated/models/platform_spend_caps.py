from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlatformSpendCaps")


@_attrs_define
class PlatformSpendCaps:
    """
    Attributes:
        operator_cap_micro (int | Unset): Set by Larynth; shown when lower than the customer cap
        tier_cap_micro (int | Unset): Verification tier cap; shown when lower than the customer cap
    """

    operator_cap_micro: int | Unset = UNSET
    tier_cap_micro: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        operator_cap_micro = self.operator_cap_micro

        tier_cap_micro = self.tier_cap_micro

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if operator_cap_micro is not UNSET:
            field_dict["operator_cap_micro"] = operator_cap_micro
        if tier_cap_micro is not UNSET:
            field_dict["tier_cap_micro"] = tier_cap_micro

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        operator_cap_micro = d.pop("operator_cap_micro", UNSET)

        tier_cap_micro = d.pop("tier_cap_micro", UNSET)

        platform_spend_caps = cls(
            operator_cap_micro=operator_cap_micro,
            tier_cap_micro=tier_cap_micro,
        )

        return platform_spend_caps
