from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ContactCallable")


@_attrs_define
class ContactCallable:
    """
    Attributes:
        informational (bool):
        marketing (bool):
    """

    informational: bool
    marketing: bool

    def to_dict(self) -> dict[str, Any]:
        informational = self.informational

        marketing = self.marketing

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "informational": informational,
                "marketing": marketing,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        informational = d.pop("informational")

        marketing = d.pop("marketing")

        contact_callable = cls(
            informational=informational,
            marketing=marketing,
        )

        return contact_callable
