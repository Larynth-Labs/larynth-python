from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="OrderNumbersItem")


@_attrs_define
class OrderNumbersItem:
    """
    Attributes:
        e164 (str):
    """

    e164: str

    def to_dict(self) -> dict[str, Any]:
        e164 = self.e164

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "e164": e164,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        e164 = d.pop("e164")

        order_numbers_item = cls(
            e164=e164,
        )

        return order_numbers_item
