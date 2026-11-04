from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="BundleLot")


@_attrs_define
class BundleLot:
    """
    Attributes:
        converts_at (datetime.datetime): Unused credit becomes normal balance at the price paid
        credit_micro (int):
        id (UUID):
        left_micro (int):
        starts_at (datetime.datetime):
    """

    converts_at: datetime.datetime
    credit_micro: int
    id: UUID
    left_micro: int
    starts_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        converts_at = self.converts_at.isoformat()

        credit_micro = self.credit_micro

        id = str(self.id)

        left_micro = self.left_micro

        starts_at = self.starts_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "converts_at": converts_at,
                "credit_micro": credit_micro,
                "id": id,
                "left_micro": left_micro,
                "starts_at": starts_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        converts_at = datetime.datetime.fromisoformat(d.pop("converts_at"))

        credit_micro = d.pop("credit_micro")

        id = UUID(d.pop("id"))

        left_micro = d.pop("left_micro")

        starts_at = datetime.datetime.fromisoformat(d.pop("starts_at"))

        bundle_lot = cls(
            converts_at=converts_at,
            credit_micro=credit_micro,
            id=id,
            left_micro=left_micro,
            starts_at=starts_at,
        )

        return bundle_lot
