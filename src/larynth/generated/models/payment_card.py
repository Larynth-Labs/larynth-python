from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PaymentCard")


@_attrs_define
class PaymentCard:
    """
    Attributes:
        brand (str):
        last4 (str):
    """

    brand: str
    last4: str

    def to_dict(self) -> dict[str, Any]:
        brand = self.brand

        last4 = self.last4

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "brand": brand,
                "last4": last4,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        brand = d.pop("brand")

        last4 = d.pop("last4")

        payment_card = cls(
            brand=brand,
            last4=last4,
        )

        return payment_card
