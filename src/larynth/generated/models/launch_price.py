from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.launch_price_applies_to_item import (
    LaunchPriceAppliesToItem,
    check_launch_price_applies_to_item,
)

T = TypeVar("T", bound="LaunchPrice")


@_attrs_define
class LaunchPrice:
    """
    Attributes:
        applies_to (list[LaunchPriceAppliesToItem]):
        ends_at (datetime.datetime): This workspace's own end date
        list_price_micro (int):
        price_micro (int):
        starts_at (datetime.datetime):
    """

    applies_to: list[LaunchPriceAppliesToItem]
    ends_at: datetime.datetime
    list_price_micro: int
    price_micro: int
    starts_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        applies_to = []
        for applies_to_item_data in self.applies_to:
            applies_to_item: str = applies_to_item_data
            applies_to.append(applies_to_item)

        ends_at = self.ends_at.isoformat()

        list_price_micro = self.list_price_micro

        price_micro = self.price_micro

        starts_at = self.starts_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "applies_to": applies_to,
                "ends_at": ends_at,
                "list_price_micro": list_price_micro,
                "price_micro": price_micro,
                "starts_at": starts_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        applies_to = []
        _applies_to = d.pop("applies_to")
        for applies_to_item_data in _applies_to:
            applies_to_item = check_launch_price_applies_to_item(applies_to_item_data)

            applies_to.append(applies_to_item)

        ends_at = datetime.datetime.fromisoformat(d.pop("ends_at"))

        list_price_micro = d.pop("list_price_micro")

        price_micro = d.pop("price_micro")

        starts_at = datetime.datetime.fromisoformat(d.pop("starts_at"))

        launch_price = cls(
            applies_to=applies_to,
            ends_at=ends_at,
            list_price_micro=list_price_micro,
            price_micro=price_micro,
            starts_at=starts_at,
        )

        return launch_price
