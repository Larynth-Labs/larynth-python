from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PracticeUsage")


@_attrs_define
class PracticeUsage:
    """
    Attributes:
        attempts_billed (int): Attempts charged this month
        attempts_free (int): Free attempts each month
        attempts_used (int): Practice call attempts that finished this month
        month (str): Month in the workspace time zone, YYYY-MM
        price_per_attempt_micro (int): Charge per attempt after the free ones, in micro-USD
    """

    attempts_billed: int
    attempts_free: int
    attempts_used: int
    month: str
    price_per_attempt_micro: int

    def to_dict(self) -> dict[str, Any]:
        attempts_billed = self.attempts_billed

        attempts_free = self.attempts_free

        attempts_used = self.attempts_used

        month = self.month

        price_per_attempt_micro = self.price_per_attempt_micro

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attempts_billed": attempts_billed,
                "attempts_free": attempts_free,
                "attempts_used": attempts_used,
                "month": month,
                "price_per_attempt_micro": price_per_attempt_micro,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        attempts_billed = d.pop("attempts_billed")

        attempts_free = d.pop("attempts_free")

        attempts_used = d.pop("attempts_used")

        month = d.pop("month")

        price_per_attempt_micro = d.pop("price_per_attempt_micro")

        practice_usage = cls(
            attempts_billed=attempts_billed,
            attempts_free=attempts_free,
            attempts_used=attempts_used,
            month=month,
            price_per_attempt_micro=price_per_attempt_micro,
        )

        return practice_usage
