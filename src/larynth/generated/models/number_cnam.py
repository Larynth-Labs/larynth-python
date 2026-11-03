from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.number_cnam_status import NumberCNAMStatus, check_number_cnam_status
from ..types import UNSET, Unset

T = TypeVar("T", bound="NumberCNAM")


@_attrs_define
class NumberCNAM:
    """
    Attributes:
        status (NumberCNAMStatus):
        name (str | Unset):
    """

    status: NumberCNAMStatus
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        status: str = self.status

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = check_number_cnam_status(d.pop("status"))

        name = d.pop("name", UNSET)

        number_cnam = cls(
            status=status,
            name=name,
        )

        return number_cnam
