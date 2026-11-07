from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.booking_defaults_approval import (
    BookingDefaultsApproval,
    check_booking_defaults_approval,
)
from ..models.booking_defaults_invite_caller import (
    BookingDefaultsInviteCaller,
    check_booking_defaults_invite_caller,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.booking_hours import BookingHours


T = TypeVar("T", bound="BookingDefaults")


@_attrs_define
class BookingDefaults:
    """
    Attributes:
        approval (BookingDefaultsApproval | Unset): Unset is direct
        buffer_min (int | Unset):
        duration_min (int | Unset):
        hold_minutes (int | Unset):
        hours (BookingHours | Unset):
        invite_caller (BookingDefaultsInviteCaller | Unset): optional: the agent offers an email invite and spells the
            address back. Unset is optional
        min_notice_min (int | Unset):
        title_template (str | Unset): Variables {{caller_name}} and {{service}}
        window_days (int | Unset):
    """

    approval: BookingDefaultsApproval | Unset = UNSET
    buffer_min: int | Unset = UNSET
    duration_min: int | Unset = UNSET
    hold_minutes: int | Unset = UNSET
    hours: BookingHours | Unset = UNSET
    invite_caller: BookingDefaultsInviteCaller | Unset = UNSET
    min_notice_min: int | Unset = UNSET
    title_template: str | Unset = UNSET
    window_days: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        approval: str | Unset = UNSET
        if not isinstance(self.approval, Unset):
            approval = self.approval

        buffer_min = self.buffer_min

        duration_min = self.duration_min

        hold_minutes = self.hold_minutes

        hours: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hours, Unset):
            hours = self.hours.to_dict()

        invite_caller: str | Unset = UNSET
        if not isinstance(self.invite_caller, Unset):
            invite_caller = self.invite_caller

        min_notice_min = self.min_notice_min

        title_template = self.title_template

        window_days = self.window_days

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if approval is not UNSET:
            field_dict["approval"] = approval
        if buffer_min is not UNSET:
            field_dict["buffer_min"] = buffer_min
        if duration_min is not UNSET:
            field_dict["duration_min"] = duration_min
        if hold_minutes is not UNSET:
            field_dict["hold_minutes"] = hold_minutes
        if hours is not UNSET:
            field_dict["hours"] = hours
        if invite_caller is not UNSET:
            field_dict["invite_caller"] = invite_caller
        if min_notice_min is not UNSET:
            field_dict["min_notice_min"] = min_notice_min
        if title_template is not UNSET:
            field_dict["title_template"] = title_template
        if window_days is not UNSET:
            field_dict["window_days"] = window_days

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.booking_hours import BookingHours

        d = dict(src_dict)
        _approval = d.pop("approval", UNSET)
        approval: BookingDefaultsApproval | Unset
        if isinstance(_approval, Unset):
            approval = UNSET
        else:
            approval = check_booking_defaults_approval(_approval)

        buffer_min = d.pop("buffer_min", UNSET)

        duration_min = d.pop("duration_min", UNSET)

        hold_minutes = d.pop("hold_minutes", UNSET)

        _hours = d.pop("hours", UNSET)
        hours: BookingHours | Unset
        if isinstance(_hours, Unset):
            hours = UNSET
        else:
            hours = BookingHours.from_dict(_hours)

        _invite_caller = d.pop("invite_caller", UNSET)
        invite_caller: BookingDefaultsInviteCaller | Unset
        if isinstance(_invite_caller, Unset):
            invite_caller = UNSET
        else:
            invite_caller = check_booking_defaults_invite_caller(_invite_caller)

        min_notice_min = d.pop("min_notice_min", UNSET)

        title_template = d.pop("title_template", UNSET)

        window_days = d.pop("window_days", UNSET)

        booking_defaults = cls(
            approval=approval,
            buffer_min=buffer_min,
            duration_min=duration_min,
            hold_minutes=hold_minutes,
            hours=hours,
            invite_caller=invite_caller,
            min_notice_min=min_notice_min,
            title_template=title_template,
            window_days=window_days,
        )

        return booking_defaults
