from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_contact_request_attributes import (
        CreateContactRequestAttributes,
    )


T = TypeVar("T", bound="CreateContactRequest")


@_attrs_define
class CreateContactRequest:
    """
    Attributes:
        e164 (str):
        attributes (CreateContactRequestAttributes | Unset):
        country (str | Unset):
        first_name (str | Unset):
        last_name (str | Unset):
        region (str | Unset):
        timezone (str | Unset):
    """

    e164: str
    attributes: CreateContactRequestAttributes | Unset = UNSET
    country: str | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    region: str | Unset = UNSET
    timezone: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        e164 = self.e164

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        country = self.country

        first_name = self.first_name

        last_name = self.last_name

        region = self.region

        timezone = self.timezone

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "e164": e164,
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
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
        from ..models.create_contact_request_attributes import (
            CreateContactRequestAttributes,
        )

        d = dict(src_dict)
        e164 = d.pop("e164")

        _attributes = d.pop("attributes", UNSET)
        attributes: CreateContactRequestAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = CreateContactRequestAttributes.from_dict(_attributes)

        country = d.pop("country", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        region = d.pop("region", UNSET)

        timezone = d.pop("timezone", UNSET)

        create_contact_request = cls(
            e164=e164,
            attributes=attributes,
            country=country,
            first_name=first_name,
            last_name=last_name,
            region=region,
            timezone=timezone,
        )

        return create_contact_request
