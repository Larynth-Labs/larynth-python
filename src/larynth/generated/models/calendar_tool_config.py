from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.booking_defaults import BookingDefaults
    from ..models.booking_service import BookingService


T = TypeVar("T", bound="CalendarToolConfig")


@_attrs_define
class CalendarToolConfig:
    """
    Attributes:
        connection_id (UUID):
        resource_id (UUID):
        overrides (BookingDefaults | Unset):
        services (list[BookingService] | Unset):
    """

    connection_id: UUID
    resource_id: UUID
    overrides: BookingDefaults | Unset = UNSET
    services: list[BookingService] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        connection_id = str(self.connection_id)

        resource_id = str(self.resource_id)

        overrides: dict[str, Any] | Unset = UNSET
        if not isinstance(self.overrides, Unset):
            overrides = self.overrides.to_dict()

        services: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()
                services.append(services_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "connection_id": connection_id,
                "resource_id": resource_id,
            }
        )
        if overrides is not UNSET:
            field_dict["overrides"] = overrides
        if services is not UNSET:
            field_dict["services"] = services

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.booking_defaults import BookingDefaults
        from ..models.booking_service import BookingService

        d = dict(src_dict)
        connection_id = UUID(d.pop("connection_id"))

        resource_id = UUID(d.pop("resource_id"))

        _overrides = d.pop("overrides", UNSET)
        overrides: BookingDefaults | Unset
        if isinstance(_overrides, Unset):
            overrides = UNSET
        else:
            overrides = BookingDefaults.from_dict(_overrides)

        _services = d.pop("services", UNSET)
        services: list[BookingService] | Unset = UNSET
        if _services is not UNSET:
            services = []
            for services_item_data in _services:
                services_item = BookingService.from_dict(services_item_data)

                services.append(services_item)

        calendar_tool_config = cls(
            connection_id=connection_id,
            resource_id=resource_id,
            overrides=overrides,
            services=services,
        )

        return calendar_tool_config
