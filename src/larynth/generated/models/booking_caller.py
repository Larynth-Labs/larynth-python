from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BookingCaller")


@_attrs_define
class BookingCaller:
    """
    Attributes:
        e164_masked (str): Caller number with the middle digits hidden
        email_masked (str | Unset):
        name (str | Unset):
    """

    e164_masked: str
    email_masked: str | Unset = UNSET
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        e164_masked = self.e164_masked

        email_masked = self.email_masked

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "e164_masked": e164_masked,
            }
        )
        if email_masked is not UNSET:
            field_dict["email_masked"] = email_masked
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        e164_masked = d.pop("e164_masked")

        email_masked = d.pop("email_masked", UNSET)

        name = d.pop("name", UNSET)

        booking_caller = cls(
            e164_masked=e164_masked,
            email_masked=email_masked,
            name=name,
        )

        return booking_caller
