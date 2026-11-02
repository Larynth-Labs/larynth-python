from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_attributes import ContactAttributes


T = TypeVar("T", bound="Contact")


@_attrs_define
class Contact:
    """
    Attributes:
        attributes (ContactAttributes):
        created_at (datetime.datetime):
        e164 (str):
        id (UUID):
        updated_at (datetime.datetime):
        country (str | Unset):
        first_name (str | Unset):
        last_name (str | Unset):
        region (str | Unset):
        timezone (str | Unset):
    """

    attributes: ContactAttributes
    created_at: datetime.datetime
    e164: str
    id: UUID
    updated_at: datetime.datetime
    country: str | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    region: str | Unset = UNSET
    timezone: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        attributes = self.attributes.to_dict()

        created_at = self.created_at.isoformat()

        e164 = self.e164

        id = str(self.id)

        updated_at = self.updated_at.isoformat()

        country = self.country

        first_name = self.first_name

        last_name = self.last_name

        region = self.region

        timezone = self.timezone

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attributes": attributes,
                "created_at": created_at,
                "e164": e164,
                "id": id,
                "updated_at": updated_at,
            }
        )
        if country is not UNSET:
            field_dict["country"] = country
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if region is not UNSET:
            field_dict["region"] = region
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.contact_attributes import ContactAttributes

        d = dict(src_dict)
        attributes = ContactAttributes.from_dict(d.pop("attributes"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        e164 = d.pop("e164")

        id = UUID(d.pop("id"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        country = d.pop("country", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        region = d.pop("region", UNSET)

        timezone = d.pop("timezone", UNSET)

        contact = cls(
            attributes=attributes,
            created_at=created_at,
            e164=e164,
            id=id,
            updated_at=updated_at,
            country=country,
            first_name=first_name,
            last_name=last_name,
            region=region,
            timezone=timezone,
        )

        return contact
