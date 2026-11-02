from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.create_contact_import_body_consent_kind import (
    CreateContactImportBodyConsentKind,
    check_create_contact_import_body_consent_kind,
)
from ..models.create_contact_import_body_consent_source import (
    CreateContactImportBodyConsentSource,
    check_create_contact_import_body_consent_source,
)
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="CreateContactImportBody")


@_attrs_define
class CreateContactImportBody:
    """
    Attributes:
        attestation_text (str): Attestation of how consent was obtained
        file (File): CSV with an e164 column; other columns become attributes
        campaign_id (UUID | Unset): Also enrol every imported contact in this campaign
        consent_kind (CreateContactImportBodyConsentKind | Unset):
        consent_source (CreateContactImportBodyConsentSource | Unset):
    """

    attestation_text: str
    file: File
    campaign_id: UUID | Unset = UNSET
    consent_kind: CreateContactImportBodyConsentKind | Unset = UNSET
    consent_source: CreateContactImportBodyConsentSource | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attestation_text = self.attestation_text

        file = self.file.to_tuple()

        campaign_id: str | Unset = UNSET
        if not isinstance(self.campaign_id, Unset):
            campaign_id = str(self.campaign_id)

        consent_kind: str | Unset = UNSET
        if not isinstance(self.consent_kind, Unset):
            consent_kind = self.consent_kind

        consent_source: str | Unset = UNSET
        if not isinstance(self.consent_source, Unset):
            consent_source = self.consent_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attestation_text": attestation_text,
                "file": file,
            }
        )
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if consent_kind is not UNSET:
            field_dict["consent_kind"] = consent_kind
        if consent_source is not UNSET:
            field_dict["consent_source"] = consent_source

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(
            (
                "attestation_text",
                (None, str(self.attestation_text).encode(), "text/plain"),
            )
        )

        files.append(("file", self.file.to_tuple()))

        if not isinstance(self.campaign_id, Unset):
            files.append(("campaign_id", (None, str(self.campaign_id), "text/plain")))

        if not isinstance(self.consent_kind, Unset):
            files.append(
                ("consent_kind", (None, str(self.consent_kind).encode(), "text/plain"))
            )

        if not isinstance(self.consent_source, Unset):
            files.append(
                (
                    "consent_source",
                    (None, str(self.consent_source).encode(), "text/plain"),
                )
            )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        attestation_text = d.pop("attestation_text")

        file = File(payload=BytesIO(d.pop("file")))

        _campaign_id = d.pop("campaign_id", UNSET)
        campaign_id: UUID | Unset
        if isinstance(_campaign_id, Unset):
            campaign_id = UNSET
        else:
            campaign_id = UUID(_campaign_id)

        _consent_kind = d.pop("consent_kind", UNSET)
        consent_kind: CreateContactImportBodyConsentKind | Unset
        if isinstance(_consent_kind, Unset):
            consent_kind = UNSET
        else:
            consent_kind = check_create_contact_import_body_consent_kind(_consent_kind)

        _consent_source = d.pop("consent_source", UNSET)
        consent_source: CreateContactImportBodyConsentSource | Unset
        if isinstance(_consent_source, Unset):
            consent_source = UNSET
        else:
            consent_source = check_create_contact_import_body_consent_source(
                _consent_source
            )

        create_contact_import_body = cls(
            attestation_text=attestation_text,
            file=file,
            campaign_id=campaign_id,
            consent_kind=consent_kind,
            consent_source=consent_source,
        )

        create_contact_import_body.additional_properties = d
        return create_contact_import_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
