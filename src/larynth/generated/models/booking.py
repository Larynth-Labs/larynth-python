from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.booking_status import BookingStatus, check_booking_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.booking_assistant import BookingAssistant
    from ..models.booking_caller import BookingCaller


T = TypeVar("T", bound="Booking")


@_attrs_define
class Booking:
    """
    Attributes:
        assistant (BookingAssistant):
        caller (BookingCaller):
        connection_id (UUID):
        created_at (datetime.datetime):
        end_at (datetime.datetime):
        id (UUID):
        invite_sent (bool): The calendar provider emailed the caller an invite
        resource_id (UUID):
        start_at (datetime.datetime):
        status (BookingStatus):
        timezone (str):
        updated_at (datetime.datetime):
        call_id (str | Unset):
        decided_by_name (str | Unset):
        notes (str | Unset):
        provider_ref (str | Unset): Opaque reference in the calendar
        reason (str | Unset):
        service (str | Unset):
    """

    assistant: BookingAssistant
    caller: BookingCaller
    connection_id: UUID
    created_at: datetime.datetime
    end_at: datetime.datetime
    id: UUID
    invite_sent: bool
    resource_id: UUID
    start_at: datetime.datetime
    status: BookingStatus
    timezone: str
    updated_at: datetime.datetime
    call_id: str | Unset = UNSET
    decided_by_name: str | Unset = UNSET
    notes: str | Unset = UNSET
    provider_ref: str | Unset = UNSET
    reason: str | Unset = UNSET
    service: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        assistant = self.assistant.to_dict()

        caller = self.caller.to_dict()

        connection_id = str(self.connection_id)

        created_at = self.created_at.isoformat()

        end_at = self.end_at.isoformat()

        id = str(self.id)

        invite_sent = self.invite_sent

        resource_id = str(self.resource_id)

        start_at = self.start_at.isoformat()

        status: str = self.status

        timezone = self.timezone

        updated_at = self.updated_at.isoformat()

        call_id = self.call_id

        decided_by_name = self.decided_by_name

        notes = self.notes

        provider_ref = self.provider_ref

        reason = self.reason

        service = self.service

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "assistant": assistant,
                "caller": caller,
                "connection_id": connection_id,
                "created_at": created_at,
                "end_at": end_at,
                "id": id,
                "invite_sent": invite_sent,
                "resource_id": resource_id,
                "start_at": start_at,
                "status": status,
                "timezone": timezone,
                "updated_at": updated_at,
            }
        )
        if call_id is not UNSET:
            field_dict["call_id"] = call_id
        if decided_by_name is not UNSET:
            field_dict["decided_by_name"] = decided_by_name
        if notes is not UNSET:
            field_dict["notes"] = notes
        if provider_ref is not UNSET:
            field_dict["provider_ref"] = provider_ref
        if reason is not UNSET:
            field_dict["reason"] = reason
        if service is not UNSET:
            field_dict["service"] = service

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.booking_assistant import BookingAssistant
        from ..models.booking_caller import BookingCaller

        d = dict(src_dict)
        assistant = BookingAssistant.from_dict(d.pop("assistant"))

        caller = BookingCaller.from_dict(d.pop("caller"))

        connection_id = UUID(d.pop("connection_id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        end_at = datetime.datetime.fromisoformat(d.pop("end_at"))

        id = UUID(d.pop("id"))

        invite_sent = d.pop("invite_sent")

        resource_id = UUID(d.pop("resource_id"))

        start_at = datetime.datetime.fromisoformat(d.pop("start_at"))

        status = check_booking_status(d.pop("status"))

        timezone = d.pop("timezone")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        call_id = d.pop("call_id", UNSET)

        decided_by_name = d.pop("decided_by_name", UNSET)

        notes = d.pop("notes", UNSET)

        provider_ref = d.pop("provider_ref", UNSET)

        reason = d.pop("reason", UNSET)

        service = d.pop("service", UNSET)

        booking = cls(
            assistant=assistant,
            caller=caller,
            connection_id=connection_id,
            created_at=created_at,
            end_at=end_at,
            id=id,
            invite_sent=invite_sent,
            resource_id=resource_id,
            start_at=start_at,
            status=status,
            timezone=timezone,
            updated_at=updated_at,
            call_id=call_id,
            decided_by_name=decided_by_name,
            notes=notes,
            provider_ref=provider_ref,
            reason=reason,
            service=service,
        )

        return booking
