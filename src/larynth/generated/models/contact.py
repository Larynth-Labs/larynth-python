from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.contact_consent_summary import (
    ContactConsentSummary,
    check_contact_consent_summary,
)
from ..models.contact_relationship import (
    ContactRelationship,
    check_contact_relationship,
)
from ..models.contact_source import ContactSource, check_contact_source
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_attributes import ContactAttributes
    from ..models.contact_callable import ContactCallable
    from ..models.contact_dnc import ContactDNC
    from ..models.contact_last_call import ContactLastCall


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
        callable_ (ContactCallable | Unset):
        consent_summary (ContactConsentSummary | Unset):
        country (str | Unset):
        dnc (ContactDNC | Unset):
        first_name (str | Unset):
        import_id (UUID | Unset):
        last_contact (ContactLastCall | Unset):
        last_name (str | Unset):
        name (str | Unset): First and last name joined; empty when unknown
        region (str | Unset):
        region_resolved (str | Unset):
        relationship (ContactRelationship | Unset): existing means an established relationship (California preamble
            rule)
        source (ContactSource | Unset):
        tags (list[str] | Unset):
        timezone (str | Unset):
        timezone_resolved (str | Unset): Contact time zone, else the area code's single zone; empty means the contact is
            not dialed
    """

    attributes: ContactAttributes
    created_at: datetime.datetime
    e164: str
    id: UUID
    updated_at: datetime.datetime
    callable_: ContactCallable | Unset = UNSET
    consent_summary: ContactConsentSummary | Unset = UNSET
    country: str | Unset = UNSET
    dnc: ContactDNC | Unset = UNSET
    first_name: str | Unset = UNSET
    import_id: UUID | Unset = UNSET
    last_contact: ContactLastCall | Unset = UNSET
    last_name: str | Unset = UNSET
    name: str | Unset = UNSET
    region: str | Unset = UNSET
    region_resolved: str | Unset = UNSET
    relationship: ContactRelationship | Unset = UNSET
    source: ContactSource | Unset = UNSET
    tags: list[str] | Unset = UNSET
    timezone: str | Unset = UNSET
    timezone_resolved: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        attributes = self.attributes.to_dict()

        created_at = self.created_at.isoformat()

        e164 = self.e164

        id = str(self.id)

        updated_at = self.updated_at.isoformat()

        callable_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.callable_, Unset):
            callable_ = self.callable_.to_dict()

        consent_summary: str | Unset = UNSET
        if not isinstance(self.consent_summary, Unset):
            consent_summary = self.consent_summary

        country = self.country

        dnc: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dnc, Unset):
            dnc = self.dnc.to_dict()

        first_name = self.first_name

        import_id: str | Unset = UNSET
        if not isinstance(self.import_id, Unset):
            import_id = str(self.import_id)

        last_contact: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_contact, Unset):
            last_contact = self.last_contact.to_dict()

        last_name = self.last_name

        name = self.name

        region = self.region

        region_resolved = self.region_resolved

        relationship: str | Unset = UNSET
        if not isinstance(self.relationship, Unset):
            relationship = self.relationship

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        timezone = self.timezone

        timezone_resolved = self.timezone_resolved

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
        if callable_ is not UNSET:
            field_dict["callable"] = callable_
        if consent_summary is not UNSET:
            field_dict["consent_summary"] = consent_summary
        if country is not UNSET:
            field_dict["country"] = country
        if dnc is not UNSET:
            field_dict["dnc"] = dnc
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if import_id is not UNSET:
            field_dict["import_id"] = import_id
        if last_contact is not UNSET:
            field_dict["last_contact"] = last_contact
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if name is not UNSET:
            field_dict["name"] = name
        if region is not UNSET:
            field_dict["region"] = region
        if region_resolved is not UNSET:
            field_dict["region_resolved"] = region_resolved
        if relationship is not UNSET:
            field_dict["relationship"] = relationship
        if source is not UNSET:
            field_dict["source"] = source
        if tags is not UNSET:
            field_dict["tags"] = tags
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if timezone_resolved is not UNSET:
            field_dict["timezone_resolved"] = timezone_resolved

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.contact_attributes import ContactAttributes
        from ..models.contact_callable import ContactCallable
        from ..models.contact_dnc import ContactDNC
        from ..models.contact_last_call import ContactLastCall

        d = dict(src_dict)
        attributes = ContactAttributes.from_dict(d.pop("attributes"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        e164 = d.pop("e164")

        id = UUID(d.pop("id"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _callable_ = d.pop("callable", UNSET)
        callable_: ContactCallable | Unset
        if isinstance(_callable_, Unset):
            callable_ = UNSET
        else:
            callable_ = ContactCallable.from_dict(_callable_)

        _consent_summary = d.pop("consent_summary", UNSET)
        consent_summary: ContactConsentSummary | Unset
        if isinstance(_consent_summary, Unset):
            consent_summary = UNSET
        else:
            consent_summary = check_contact_consent_summary(_consent_summary)

        country = d.pop("country", UNSET)

        _dnc = d.pop("dnc", UNSET)
        dnc: ContactDNC | Unset
        if isinstance(_dnc, Unset):
            dnc = UNSET
        else:
            dnc = ContactDNC.from_dict(_dnc)

        first_name = d.pop("first_name", UNSET)

        _import_id = d.pop("import_id", UNSET)
        import_id: UUID | Unset
        if isinstance(_import_id, Unset):
            import_id = UNSET
        else:
            import_id = UUID(_import_id)

        _last_contact = d.pop("last_contact", UNSET)
        last_contact: ContactLastCall | Unset
        if isinstance(_last_contact, Unset):
            last_contact = UNSET
        else:
            last_contact = ContactLastCall.from_dict(_last_contact)

        last_name = d.pop("last_name", UNSET)

        name = d.pop("name", UNSET)

        region = d.pop("region", UNSET)

        region_resolved = d.pop("region_resolved", UNSET)

        _relationship = d.pop("relationship", UNSET)
        relationship: ContactRelationship | Unset
        if isinstance(_relationship, Unset):
            relationship = UNSET
        else:
            relationship = check_contact_relationship(_relationship)

        _source = d.pop("source", UNSET)
        source: ContactSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_contact_source(_source)

        tags = cast(list[str], d.pop("tags", UNSET))

        timezone = d.pop("timezone", UNSET)

        timezone_resolved = d.pop("timezone_resolved", UNSET)

        contact = cls(
            attributes=attributes,
            created_at=created_at,
            e164=e164,
            id=id,
            updated_at=updated_at,
            callable_=callable_,
            consent_summary=consent_summary,
            country=country,
            dnc=dnc,
            first_name=first_name,
            import_id=import_id,
            last_contact=last_contact,
            last_name=last_name,
            name=name,
            region=region,
            region_resolved=region_resolved,
            relationship=relationship,
            source=source,
            tags=tags,
            timezone=timezone,
            timezone_resolved=timezone_resolved,
        )

        return contact
