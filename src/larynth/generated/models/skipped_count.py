from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.skipped_count_reason_code import (
    SkippedCountReasonCode,
    check_skipped_count_reason_code,
)

T = TypeVar("T", bound="SkippedCount")


@_attrs_define
class SkippedCount:
    """
    Attributes:
        count (int):
        reason_code (SkippedCountReasonCode):
    """

    count: int
    reason_code: SkippedCountReasonCode

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        reason_code: str = self.reason_code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
                "reason_code": reason_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        count = d.pop("count")

        reason_code = check_skipped_count_reason_code(d.pop("reason_code"))

        skipped_count = cls(
            count=count,
            reason_code=reason_code,
        )

        return skipped_count
