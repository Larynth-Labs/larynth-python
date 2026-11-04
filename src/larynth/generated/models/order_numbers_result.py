from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.number import Number


T = TypeVar("T", bound="OrderNumbersResult")


@_attrs_define
class OrderNumbersResult:
    """
    Attributes:
        due_now_micro (int): First month of every number, charged from the paid balance as each provisions
        monthly_micro (int):
        numbers (list[Number]):
    """

    due_now_micro: int
    monthly_micro: int
    numbers: list[Number]

    def to_dict(self) -> dict[str, Any]:
        due_now_micro = self.due_now_micro

        monthly_micro = self.monthly_micro

        numbers = []
        for numbers_item_data in self.numbers:
            numbers_item = numbers_item_data.to_dict()
            numbers.append(numbers_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "due_now_micro": due_now_micro,
                "monthly_micro": monthly_micro,
                "numbers": numbers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.number import Number

        d = dict(src_dict)
        due_now_micro = d.pop("due_now_micro")

        monthly_micro = d.pop("monthly_micro")

        numbers = []
        _numbers = d.pop("numbers")
        for numbers_item_data in _numbers:
            numbers_item = Number.from_dict(numbers_item_data)

            numbers.append(numbers_item)

        order_numbers_result = cls(
            due_now_micro=due_now_micro,
            monthly_micro=monthly_micro,
            numbers=numbers,
        )

        return order_numbers_result
