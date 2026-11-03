from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.number_branded_status import (
    NumberBrandedStatus,
    check_number_branded_status,
)

T = TypeVar("T", bound="NumberBranded")


@_attrs_define
class NumberBranded:
    """
    Attributes:
        status (NumberBrandedStatus):
    """

    status: NumberBrandedStatus

    def to_dict(self) -> dict[str, Any]:
        status: str = self.status

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = check_number_branded_status(d.pop("status"))

        number_branded = cls(
            status=status,
        )

        return number_branded
