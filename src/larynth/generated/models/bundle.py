from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="Bundle")


@_attrs_define
class Bundle:
    """
    Attributes:
        credit_micro (int):
        discount_bp (int): Discount in basis points of the credit
        key (str):
        minutes_estimate (int): Credit divided by this workspace's current agent minute price, rounded down
        name_key (str):
        price_micro (int):
        sort (int):
    """

    credit_micro: int
    discount_bp: int
    key: str
    minutes_estimate: int
    name_key: str
    price_micro: int
    sort: int

    def to_dict(self) -> dict[str, Any]:
        credit_micro = self.credit_micro

        discount_bp = self.discount_bp

        key = self.key

        minutes_estimate = self.minutes_estimate

        name_key = self.name_key

        price_micro = self.price_micro

        sort = self.sort

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "credit_micro": credit_micro,
                "discount_bp": discount_bp,
                "key": key,
                "minutes_estimate": minutes_estimate,
                "name_key": name_key,
                "price_micro": price_micro,
                "sort": sort,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        credit_micro = d.pop("credit_micro")

        discount_bp = d.pop("discount_bp")

        key = d.pop("key")

        minutes_estimate = d.pop("minutes_estimate")

        name_key = d.pop("name_key")

        price_micro = d.pop("price_micro")

        sort = d.pop("sort")

        bundle = cls(
            credit_micro=credit_micro,
            discount_bp=discount_bp,
            key=key,
            minutes_estimate=minutes_estimate,
            name_key=name_key,
            price_micro=price_micro,
            sort=sort,
        )

        return bundle
