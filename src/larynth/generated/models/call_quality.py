from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.call_quality_check import CallQualityCheck


T = TypeVar("T", bound="CallQuality")


@_attrs_define
class CallQuality:
    """
    Attributes:
        checked_at (datetime.datetime):
        checks (list[CallQualityCheck]):
        score (int):
    """

    checked_at: datetime.datetime
    checks: list[CallQualityCheck]
    score: int

    def to_dict(self) -> dict[str, Any]:
        checked_at = self.checked_at.isoformat()

        checks = []
        for checks_item_data in self.checks:
            checks_item = checks_item_data.to_dict()
            checks.append(checks_item)

        score = self.score

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "checked_at": checked_at,
                "checks": checks,
                "score": score,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.call_quality_check import CallQualityCheck

        d = dict(src_dict)
        checked_at = datetime.datetime.fromisoformat(d.pop("checked_at"))

        checks = []
        _checks = d.pop("checks")
        for checks_item_data in _checks:
            checks_item = CallQualityCheck.from_dict(checks_item_data)

            checks.append(checks_item)

        score = d.pop("score")

        call_quality = cls(
            checked_at=checked_at,
            checks=checks,
            score=score,
        )

        return call_quality
