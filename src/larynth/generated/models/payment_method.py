from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.payment_method_used_by_item import (
    PaymentMethodUsedByItem,
    check_payment_method_used_by_item,
)

T = TypeVar("T", bound="PaymentMethod")


@_attrs_define
class PaymentMethod:
    """
    Attributes:
        brand (str):
        created_at (datetime.datetime):
        exp_month (int):
        exp_year (int):
        id (str): Payment provider id; opaque
        is_default (bool):
        last4 (str):
        used_by (list[PaymentMethodUsedByItem]):
    """

    brand: str
    created_at: datetime.datetime
    exp_month: int
    exp_year: int
    id: str
    is_default: bool
    last4: str
    used_by: list[PaymentMethodUsedByItem]

    def to_dict(self) -> dict[str, Any]:
        brand = self.brand

        created_at = self.created_at.isoformat()

        exp_month = self.exp_month

        exp_year = self.exp_year

        id = self.id

        is_default = self.is_default

        last4 = self.last4

        used_by = []
        for used_by_item_data in self.used_by:
            used_by_item: str = used_by_item_data
            used_by.append(used_by_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "brand": brand,
                "created_at": created_at,
                "exp_month": exp_month,
                "exp_year": exp_year,
                "id": id,
                "is_default": is_default,
                "last4": last4,
                "used_by": used_by,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        brand = d.pop("brand")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        exp_month = d.pop("exp_month")

        exp_year = d.pop("exp_year")

        id = d.pop("id")

        is_default = d.pop("is_default")

        last4 = d.pop("last4")

        used_by = []
        _used_by = d.pop("used_by")
        for used_by_item_data in _used_by:
            used_by_item = check_payment_method_used_by_item(used_by_item_data)

            used_by.append(used_by_item)

        payment_method = cls(
            brand=brand,
            created_at=created_at,
            exp_month=exp_month,
            exp_year=exp_year,
            id=id,
            is_default=is_default,
            last4=last4,
            used_by=used_by,
        )

        return payment_method
