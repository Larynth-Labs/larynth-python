from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.booking_defaults import BookingDefaults


T = TypeVar("T", bound="UpdateCalendarConnectionRequest")


@_attrs_define
class UpdateCalendarConnectionRequest:
    """
    Attributes:
        defaults (BookingDefaults | Unset):
        label (str | Unset):
    """

    defaults: BookingDefaults | Unset = UNSET
    label: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        defaults: dict[str, Any] | Unset = UNSET
        if not isinstance(self.defaults, Unset):
            defaults = self.defaults.to_dict()

        label = self.label

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if defaults is not UNSET:
            field_dict["defaults"] = defaults
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.booking_defaults import BookingDefaults

        d = dict(src_dict)
        _defaults = d.pop("defaults", UNSET)
        defaults: BookingDefaults | Unset
        if isinstance(_defaults, Unset):
            defaults = UNSET
        else:
            defaults = BookingDefaults.from_dict(_defaults)

        label = d.pop("label", UNSET)

        update_calendar_connection_request = cls(
            defaults=defaults,
            label=label,
        )

        return update_calendar_connection_request
