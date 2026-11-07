from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.calendar_resource_kind import (
    CalendarResourceKind,
    check_calendar_resource_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CalendarResource")


@_attrs_define
class CalendarResource:
    """
    Attributes:
        external_id (str):
        id (UUID):
        kind (CalendarResourceKind):
        name (str):
        timezone (str):
        duration_min (int | Unset):
    """

    external_id: str
    id: UUID
    kind: CalendarResourceKind
    name: str
    timezone: str
    duration_min: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        external_id = self.external_id

        id = str(self.id)

        kind: str = self.kind

        name = self.name

        timezone = self.timezone

        duration_min = self.duration_min

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "external_id": external_id,
                "id": id,
                "kind": kind,
                "name": name,
                "timezone": timezone,
            }
        )
        if duration_min is not UNSET:
            field_dict["duration_min"] = duration_min

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        external_id = d.pop("external_id")

        id = UUID(d.pop("id"))

        kind = check_calendar_resource_kind(d.pop("kind"))

        name = d.pop("name")

        timezone = d.pop("timezone")

        duration_min = d.pop("duration_min", UNSET)

        calendar_resource = cls(
            external_id=external_id,
            id=id,
            kind=kind,
            name=name,
            timezone=timezone,
            duration_min=duration_min,
        )

        return calendar_resource
