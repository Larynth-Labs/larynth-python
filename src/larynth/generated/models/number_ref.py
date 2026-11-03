from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NumberRef")


@_attrs_define
class NumberRef:
    """
    Attributes:
        e164 (str):
        id (UUID):
        label (str | Unset):
    """

    e164: str
    id: UUID
    label: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        e164 = self.e164

        id = str(self.id)

        label = self.label

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "e164": e164,
                "id": id,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        e164 = d.pop("e164")

        id = UUID(d.pop("id"))

        label = d.pop("label", UNSET)

        number_ref = cls(
            e164=e164,
            id=id,
            label=label,
        )

        return number_ref
