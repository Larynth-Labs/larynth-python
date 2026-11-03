from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.number_route_type import NumberRouteType, check_number_route_type
from ..models.number_status import NumberStatus, check_number_status
from ..types import UNSET, Unset

T = TypeVar("T", bound="Number")


@_attrs_define
class Number:
    """
    Attributes:
        country (str):
        created_at (datetime.datetime):
        e164 (str):
        id (UUID):
        monthly_price_micro (int):
        route_type (NumberRouteType):
        status (NumberStatus):
        updated_at (datetime.datetime):
        assistant_id (UUID | Unset):
        forward_to_e164 (str | Unset):
        label (str | Unset):
        purchased_at (datetime.datetime | Unset):
        region (str | Unset):
        released_at (datetime.datetime | Unset):
    """

    country: str
    created_at: datetime.datetime
    e164: str
    id: UUID
    monthly_price_micro: int
    route_type: NumberRouteType
    status: NumberStatus
    updated_at: datetime.datetime
    assistant_id: UUID | Unset = UNSET
    forward_to_e164: str | Unset = UNSET
    label: str | Unset = UNSET
    purchased_at: datetime.datetime | Unset = UNSET
    region: str | Unset = UNSET
    released_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        country = self.country

        created_at = self.created_at.isoformat()

        e164 = self.e164

        id = str(self.id)

        monthly_price_micro = self.monthly_price_micro

        route_type: str = self.route_type

        status: str = self.status

        updated_at = self.updated_at.isoformat()

        assistant_id: str | Unset = UNSET
        if not isinstance(self.assistant_id, Unset):
            assistant_id = str(self.assistant_id)

        forward_to_e164 = self.forward_to_e164

        label = self.label

        purchased_at: str | Unset = UNSET
        if not isinstance(self.purchased_at, Unset):
            purchased_at = self.purchased_at.isoformat()

        region = self.region

        released_at: str | Unset = UNSET
        if not isinstance(self.released_at, Unset):
            released_at = self.released_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "country": country,
                "created_at": created_at,
                "e164": e164,
                "id": id,
                "monthly_price_micro": monthly_price_micro,
                "route_type": route_type,
                "status": status,
                "updated_at": updated_at,
            }
        )
        if assistant_id is not UNSET:
            field_dict["assistant_id"] = assistant_id
        if forward_to_e164 is not UNSET:
            field_dict["forward_to_e164"] = forward_to_e164
        if label is not UNSET:
            field_dict["label"] = label
        if purchased_at is not UNSET:
            field_dict["purchased_at"] = purchased_at
        if region is not UNSET:
            field_dict["region"] = region
        if released_at is not UNSET:
            field_dict["released_at"] = released_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        country = d.pop("country")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        e164 = d.pop("e164")

        id = UUID(d.pop("id"))

        monthly_price_micro = d.pop("monthly_price_micro")

        route_type = check_number_route_type(d.pop("route_type"))

        status = check_number_status(d.pop("status"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _assistant_id = d.pop("assistant_id", UNSET)
        assistant_id: UUID | Unset
        if isinstance(_assistant_id, Unset):
            assistant_id = UNSET
        else:
            assistant_id = UUID(_assistant_id)

        forward_to_e164 = d.pop("forward_to_e164", UNSET)

        label = d.pop("label", UNSET)

        _purchased_at = d.pop("purchased_at", UNSET)
        purchased_at: datetime.datetime | Unset
        if isinstance(_purchased_at, Unset):
            purchased_at = UNSET
        else:
            purchased_at = datetime.datetime.fromisoformat(_purchased_at)

        region = d.pop("region", UNSET)

        _released_at = d.pop("released_at", UNSET)
        released_at: datetime.datetime | Unset
        if isinstance(_released_at, Unset):
            released_at = UNSET
        else:
            released_at = datetime.datetime.fromisoformat(_released_at)

        number = cls(
            country=country,
            created_at=created_at,
            e164=e164,
            id=id,
            monthly_price_micro=monthly_price_micro,
            route_type=route_type,
            status=status,
            updated_at=updated_at,
            assistant_id=assistant_id,
            forward_to_e164=forward_to_e164,
            label=label,
            purchased_at=purchased_at,
            region=region,
            released_at=released_at,
        )

        return number
