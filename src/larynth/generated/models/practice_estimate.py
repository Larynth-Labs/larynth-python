from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PracticeEstimate")


@_attrs_define
class PracticeEstimate:
    """
    Attributes:
        attempts (int):
        billable_micro (int):
        free_left (int):
    """

    attempts: int
    billable_micro: int
    free_left: int

    def to_dict(self) -> dict[str, Any]:
        attempts = self.attempts

        billable_micro = self.billable_micro

        free_left = self.free_left

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attempts": attempts,
                "billable_micro": billable_micro,
                "free_left": free_left,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        attempts = d.pop("attempts")

        billable_micro = d.pop("billable_micro")

        free_left = d.pop("free_left")

        practice_estimate = cls(
            attempts=attempts,
            billable_micro=billable_micro,
            free_left=free_left,
        )

        return practice_estimate
