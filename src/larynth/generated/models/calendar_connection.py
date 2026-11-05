from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.calendar_connection_status import (
    CalendarConnectionStatus,
    check_calendar_connection_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.booking_defaults import BookingDefaults
    from ..models.calendar_resource import CalendarResource
    from ..models.integration_provider import IntegrationProvider
    from ..models.tool_use import ToolUse


T = TypeVar("T", bound="CalendarConnection")


@_attrs_define
class CalendarConnection:
    """
    Attributes:
        account_label (str):
        created_at (datetime.datetime):
        defaults (BookingDefaults):
        id (UUID):
        provider (IntegrationProvider):
        resources (list[CalendarResource]):
        status (CalendarConnectionStatus):
        used_by (list[ToolUse]):
        connected_by_name (str | Unset):
    """

    account_label: str
    created_at: datetime.datetime
    defaults: BookingDefaults
    id: UUID
    provider: IntegrationProvider
    resources: list[CalendarResource]
    status: CalendarConnectionStatus
    used_by: list[ToolUse]
    connected_by_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        account_label = self.account_label

        created_at = self.created_at.isoformat()

        defaults = self.defaults.to_dict()

        id = str(self.id)

        provider = self.provider.to_dict()

        resources = []
        for resources_item_data in self.resources:
            resources_item = resources_item_data.to_dict()
            resources.append(resources_item)

        status: str = self.status

        used_by = []
        for used_by_item_data in self.used_by:
            used_by_item = used_by_item_data.to_dict()
            used_by.append(used_by_item)

        connected_by_name = self.connected_by_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "account_label": account_label,
                "created_at": created_at,
                "defaults": defaults,
                "id": id,
                "provider": provider,
                "resources": resources,
                "status": status,
                "used_by": used_by,
            }
        )
        if connected_by_name is not UNSET:
            field_dict["connected_by_name"] = connected_by_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.booking_defaults import BookingDefaults
        from ..models.calendar_resource import CalendarResource
        from ..models.integration_provider import IntegrationProvider
        from ..models.tool_use import ToolUse

        d = dict(src_dict)
        account_label = d.pop("account_label")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        defaults = BookingDefaults.from_dict(d.pop("defaults"))

        id = UUID(d.pop("id"))

        provider = IntegrationProvider.from_dict(d.pop("provider"))

        resources = []
        _resources = d.pop("resources")
        for resources_item_data in _resources:
            resources_item = CalendarResource.from_dict(resources_item_data)

            resources.append(resources_item)

        status = check_calendar_connection_status(d.pop("status"))

        used_by = []
        _used_by = d.pop("used_by")
        for used_by_item_data in _used_by:
            used_by_item = ToolUse.from_dict(used_by_item_data)

            used_by.append(used_by_item)

        connected_by_name = d.pop("connected_by_name", UNSET)

        calendar_connection = cls(
            account_label=account_label,
            created_at=created_at,
            defaults=defaults,
            id=id,
            provider=provider,
            resources=resources,
            status=status,
            used_by=used_by,
            connected_by_name=connected_by_name,
        )

        return calendar_connection
