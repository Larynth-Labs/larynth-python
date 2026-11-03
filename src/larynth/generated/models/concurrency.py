from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="Concurrency")


@_attrs_define
class Concurrency:
    """
    Attributes:
        in_use (int):
        limit (int):
    """

    in_use: int
    limit: int

    def to_dict(self) -> dict[str, Any]:
        in_use = self.in_use

        limit = self.limit

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "in_use": in_use,
                "limit": limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        in_use = d.pop("in_use")

        limit = d.pop("limit")

        concurrency = cls(
            in_use=in_use,
            limit=limit,
        )

        return concurrency
