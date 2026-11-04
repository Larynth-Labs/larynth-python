from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.preflight_check import PreflightCheck


T = TypeVar("T", bound="PreflightResult")


@_attrs_define
class PreflightResult:
    """
    Attributes:
        can_launch (bool):
        checks (list[PreflightCheck]):
    """

    can_launch: bool
    checks: list[PreflightCheck]

    def to_dict(self) -> dict[str, Any]:
        can_launch = self.can_launch

        checks = []
        for checks_item_data in self.checks:
            checks_item = checks_item_data.to_dict()
            checks.append(checks_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "can_launch": can_launch,
                "checks": checks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.preflight_check import PreflightCheck

        d = dict(src_dict)
        can_launch = d.pop("can_launch")

        checks = []
        _checks = d.pop("checks")
        for checks_item_data in _checks:
            checks_item = PreflightCheck.from_dict(checks_item_data)

            checks.append(checks_item)

        preflight_result = cls(
            can_launch=can_launch,
            checks=checks,
        )

        return preflight_result
