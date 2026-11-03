from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ComparePrice")


@_attrs_define
class ComparePrice:
    """
    Attributes:
        after_micro_per_min (int):
        before_micro_per_min (int):
    """

    after_micro_per_min: int
    before_micro_per_min: int

    def to_dict(self) -> dict[str, Any]:
        after_micro_per_min = self.after_micro_per_min

        before_micro_per_min = self.before_micro_per_min

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "after_micro_per_min": after_micro_per_min,
                "before_micro_per_min": before_micro_per_min,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        after_micro_per_min = d.pop("after_micro_per_min")

        before_micro_per_min = d.pop("before_micro_per_min")

        compare_price = cls(
            after_micro_per_min=after_micro_per_min,
            before_micro_per_min=before_micro_per_min,
        )

        return compare_price
