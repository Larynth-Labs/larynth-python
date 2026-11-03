from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SimulationsSummary")


@_attrs_define
class SimulationsSummary:
    """
    Attributes:
        passed (int):
        total (int):
    """

    passed: int
    total: int

    def to_dict(self) -> dict[str, Any]:
        passed = self.passed

        total = self.total

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "passed": passed,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        passed = d.pop("passed")

        total = d.pop("total")

        simulations_summary = cls(
            passed=passed,
            total=total,
        )

        return simulations_summary
