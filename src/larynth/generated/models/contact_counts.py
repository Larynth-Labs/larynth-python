from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ContactCounts")


@_attrs_define
class ContactCounts:
    """
    Attributes:
        all_ (int):
        callable_ (int):
        dnc (int):
        needs_consent (int):
    """

    all_: int
    callable_: int
    dnc: int
    needs_consent: int

    def to_dict(self) -> dict[str, Any]:
        all_ = self.all_

        callable_ = self.callable_

        dnc = self.dnc

        needs_consent = self.needs_consent

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "all": all_,
                "callable": callable_,
                "dnc": dnc,
                "needs_consent": needs_consent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        all_ = d.pop("all")

        callable_ = d.pop("callable")

        dnc = d.pop("dnc")

        needs_consent = d.pop("needs_consent")

        contact_counts = cls(
            all_=all_,
            callable_=callable_,
            dnc=dnc,
            needs_consent=needs_consent,
        )

        return contact_counts
